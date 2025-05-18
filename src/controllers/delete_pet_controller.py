from src.models.interfaces.repositories.pets_repository import PetsRepositoryInterface

from .interfaces.delete_pet_controller_interface import DeletePetControllerInterface

class DeletePetController(DeletePetControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    def execute(self, pet_name: str) -> None:
        self.__validate_input(pet_name)

        self.__pets_repository.delete_pets(pet_name)


    def __validate_input(self, pet_name: str) -> None:
        if not isinstance(pet_name, str):
            raise Exception('Invalid Pet name')
        