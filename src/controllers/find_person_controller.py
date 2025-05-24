from src.models.interfaces.repositories.people_repository import PeopleRepositoryInterface
from src.models.interfaces.entities.people import PeopleInterface
from src.errors.types.http_not_found import HttpNotFoundError

from .interfaces.find_person_controller_interface import (
  FindPersonControllerInterface, FormattedResponse
)

class FindPersonController(FindPersonControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository


    def execute(self, person_id: int) -> FormattedResponse:
        self.__validate_input(person_id)

        found_person = self.__people_repository.get_person(person_id)

        if not found_person:
            raise Exception('Person not found')

        formatted_response = self.__format_response(found_person)

        return formatted_response


    def __validate_input(self, person_id: int) -> None:
        if not isinstance(person_id, int):
            raise HttpNotFoundError('Invalid id')

    def __format_response(self, person: PeopleInterface) -> dict:
        return {
            'data': {
                'type': 'Person',
                'count': 1,
                'attributes': {
                    'first_name': person.first_name,
                    'last_name': person.last_name,
                    'pet_name': person.pet_name,
                    'pet_type': person.pet_type
                }
            }
        }
    