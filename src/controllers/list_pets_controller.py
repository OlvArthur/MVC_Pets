from typing import TypedDict

from src.models.interfaces.repositories.pets_repository import PetsRepositoryInterface
from src.models.interfaces.entities.pets import PetsInterface


class FormattedResponseData(TypedDict):
    type: str
    count: int
    attributes: list[PetsInterface]

class FormattedResponse(TypedDict):
    data : FormattedResponseData



class ListPetsController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def execute(self) -> FormattedResponse:
        pets =  self.__pets_repository.list_pets()

        formatted_respone = self.__format_response(pets)

        return formatted_respone



    def __format_response(self, pets: list[PetsInterface]) -> FormattedResponse:
        return {
            'data': {
                'type': 'Pet',
                'count': len(pets),
                'attributes': [{'name': pet.name, 'type': pet.type } for pet in pets]
            }
        }
        