from abc import abstractmethod
from .base_interface import BaseControllerInterface, FormattedResponse


class CreatePersonControllerInterface(BaseControllerInterface):

    @abstractmethod
    def execute(self, person_info: dict) -> FormattedResponse: pass
