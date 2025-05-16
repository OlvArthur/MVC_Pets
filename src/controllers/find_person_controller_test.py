from src.controllers.find_person_controller import FindPersonController

class PersonMock():
    def __init__(self, first_name: str, last_name: str, pet_name: str, pet_type: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type



class PersonRepositoryMock:
    def get_person(self, person_id: int):
        people = {
            1: PersonMock(
                first_name='jhon',
                last_name= 'Doe',
                pet_name= 'Doggie',
                pet_type= 'dog'
            )
        }

        if person_id not in people:
            return None

        return people[person_id]

def test_find_person():
    repo_mock = PersonRepositoryMock()
    controller = FindPersonController(repo_mock)

    response = controller.execute(1)

    assert response['data']['count'] == 1
    assert response['data']['type'] == 'Person'
    assert response['data']['attributes']['first_name'] == 'jhon'
    assert response['data']['attributes']['last_name'] == 'Doe'
