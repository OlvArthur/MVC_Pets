from abc import ABC, abstractmethod
from src.models.interfaces.entities.people import PeopleInterface

class PeopleRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, first_name:str, last_name: str, age: int, pet_id: int) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PeopleInterface | None:
        pass
    