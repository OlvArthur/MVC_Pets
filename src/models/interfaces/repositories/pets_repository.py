from abc import ABC, abstractmethod
# from src.models.interfaces.entities.pets import
# from src.models.interfaces.entities.pets import PetsInterface


class PetsRepositoryInterface(ABC):

    # @abstractmethod
    # def list_pets(self) -> list[PetsInterface]: pass

    @abstractmethod
    def delete_pets(self, pet_name: str) -> None: pass

    @abstractmethod
    def find_pet_by_name(self, pet_name: str) -> None: pass
