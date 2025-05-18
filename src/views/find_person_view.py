from src.controllers.interfaces.find_person_controller_interface import (
   FindPersonControllerInterface
)
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class FindPersonView(ViewInterface):
    def __init__(self, controller: FindPersonControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.params['id']
        body_response = self.__controller.execute(person_id)

        return HttpResponse(status_code=200, body=body_response)
