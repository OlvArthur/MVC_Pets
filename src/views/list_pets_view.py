from src.controllers.interfaces.base_interface import (
   BaseControllerInterface
)
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class ListPetsView(ViewInterface):
    def __init__(self, controller: BaseControllerInterface):
        self.__controller = controller

    def handle(self, _: HttpRequest) -> HttpResponse:
        body_response = self.__controller.execute()

        return HttpResponse(status_code=200, body=body_response)
