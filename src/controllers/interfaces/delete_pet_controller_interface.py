
from abc import abstractmethod
from .base_interface import BaseControllerInterface

class DeletePetControllerInterface(BaseControllerInterface):

    @abstractmethod
    def execute(self, pet_name: str) -> None: pass
