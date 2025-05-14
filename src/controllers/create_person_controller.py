from src.models.interfaces.repositories.people_repository import PeopleRepositoryInterface
from src.models.interfaces.entities.people import PeopleInterface

class CreatePersonController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def execute(self, first_name: str, last_name: str, age: int, pet_id: int) -> PeopleInterface:
        new_person = self.__people_repository.insert_person(first_name, last_name, age, pet_id)
        return new_person
