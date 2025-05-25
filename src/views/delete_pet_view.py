from src.controllers.interfaces.delete_pet_controller_interface import DeletePetControllerInterface
from src.views.validators.delete_pet_validator import (
  delete_pet_validator as validate_request_params
)

from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class DeletePetView(ViewInterface):
    def __init__(self, controller: DeletePetControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        validate_request_params(http_request)
        pet_name = http_request.params['name']
        self.__controller.execute(pet_name)

        return HttpResponse(status_code=204)
