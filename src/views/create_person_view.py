from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.create_person_controller_interface import (
  CreatePersonControllerInterface
)

from .validators.create_person_validator import create_person_validator as validate_request_body
from .interfaces.view_interface import ViewInterface


class CreatePersonView(ViewInterface):
    def __init__(self, controller: CreatePersonControllerInterface):
        self.__controller = controller


    def handle(self, http_request: HttpRequest) -> HttpResponse:
        validate_request_body(http_request)
        person_info = http_request.body
        body_response = self.__controller.execute(person_info)

        return HttpResponse(status_code=201, body=body_response)
