from pytest import raises

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from .create_person_validator import create_person_validator

class RequestMock:
    def __init__(self, body):
        self.body = body

def test_create_person_validator():
    request = RequestMock({
        'first_name': 'john',
        'age': 32,
        'pet_id': 2
    })

    with raises(HttpUnprocessableEntityError):
        create_person_validator(request)
