from src.models.interfaces.entities.pets import PetsInterface
from .list_pets_controller import ListPetsController

class PetMock:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type


class PetsReposioryMock:
    def __init__(self):
        self.pets = [
            PetMock('shrek', 'dog'),
            PetMock('baby', 'shark'),
            PetMock('jorgin', 'hamster')
        ]

    def list_pets(self) -> list[PetsInterface]:
        return self.pets

def test_list_pets():
    repo_mock = PetsReposioryMock()
    controller = ListPetsController(repo_mock)

    response = controller.execute()

    expected_response = [
        {'name': pet.name, 'type': pet.type } for pet in repo_mock.pets
    ]

    assert response['data']['attributes'] == expected_response
    assert response['data']['type'] == 'Pet'
