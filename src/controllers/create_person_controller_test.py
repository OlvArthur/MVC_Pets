from typing import TypedDict
import pytest

from .create_person_controller import CreatePersonController


class PeopleRepositoryMock:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int): pass


class SetupVariables(TypedDict):
    repo_mock = PeopleRepositoryMock
    controller: CreatePersonController

@pytest.fixture
def setup() -> SetupVariables: # type: ignore
    people_repository_mock = PeopleRepositoryMock()
    controller = CreatePersonController(people_repository_mock)

    setup_variables = {
        'repo_mock': people_repository_mock,
        'controller': controller
    }

    yield setup_variables


def test_create_person(setup):
    person_info = {
        'first_name': 'jhon',
        'last_name': 'Doe',
        'age': 32,
        'pet_id': 2
    }

    response = setup['controller'].execute(person_info)

    assert response['data']['count'] == 1
    assert response['data']['type'] == 'Person'
    assert response['data']['attributes'] == person_info


def test_validate_names(setup):
    person_info = {
        'first_name': 'Invalid first name',
        'last_name': 'Doe',
        'age': 32,
        'pet_id': 3
    }

    with pytest.raises(Exception) as exc1:
        setup['controller'].execute(person_info)

    assert str(exc1.value) == 'Invalid person name'

    person_info['first_name'] = 'jhon'
    person_info['last_name'] = 'Invalid last name'

    with pytest.raises(Exception) as exc2:
        setup['controller'].execute(person_info)


    assert str(exc2.value) == 'Invalid person name'
