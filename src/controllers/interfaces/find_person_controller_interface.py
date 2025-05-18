from abc import abstractmethod
from .base_interface import BaseControllerInterface, FormattedResponse

class FindPersonControllerInterface(BaseControllerInterface):

    @abstractmethod
    def execute(self, person_id: int) -> FormattedResponse: pass
