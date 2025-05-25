from src.models.interfaces.repositories.pets_repository import PetsRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError

from .interfaces.delete_pet_controller_interface import DeletePetControllerInterface

class DeletePetController(DeletePetControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.__pets_repository = pets_repository

    def execute(self, pet_name: str) -> None:
        self.__validate_input(pet_name)

        self.__verify_pet_exists(pet_name)

        self.__pets_repository.delete_pets(pet_name)


    def __validate_input(self, pet_name: str) -> None:
        if not isinstance(pet_name, str):
            raise HttpBadRequestError('Invalid Pet name')

    def __verify_pet_exists(self, pet_name: str) -> None:
        found_pet = self.__pets_repository.find_pet_by_name(pet_name)

        if not found_pet:
            raise HttpNotFoundError('Pet not found')
