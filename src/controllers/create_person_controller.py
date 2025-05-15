import re
from typing import TypedDict

from src.models.interfaces.repositories.people_repository import PeopleRepositoryInterface

class FormattedResponseData(TypedDict):
    type: str
    count: int
    attributes: dict

class FormattedResponse(TypedDict):
    data: FormattedResponseData
class CreatePersonController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.__people_repository = people_repository

    def execute(self, person_info: dict) -> FormattedResponse:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_names(first_name, last_name)

        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

        formatted_response = self.__format_response(person_info)

        return formatted_response


    def __validate_names(self, first_name: str, last_name: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise Exception("Invalid person name")

    def __format_response(self, person_info: dict) -> FormattedResponse:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
