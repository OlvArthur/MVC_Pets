from typing import TypedDict
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.people import PeopleTable
from .people_repository import PeopleRepository

db_connection_handler.connect_to_db()

class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass



class SetupVariables(TypedDict):
    repo: PeopleRepository
    connection_handler_mock: ConnectionHandlerMock


@pytest.fixture
def setup() -> SetupVariables:  # type: ignore
    db_connection_handler_mock = ConnectionHandlerMock()
    repo = PeopleRepository(db_connection_handler_mock)


    setup_variables = {
        'repo': repo,
        'connection_handler_mock': db_connection_handler_mock
    }

    yield setup_variables

def test_insert_person(setup):
    setup['repo'].insert_person(
        first_name='john',
        last_name='Doe', pet_id=1, age=32)

    setup['connection_handler_mock'].session.add.assert_called()
    assert isinstance(setup['connection_handler_mock'].session.add.call_args[0][0], PeopleTable)
    assert setup['connection_handler_mock'].session.add.call_args[0][0].first_name == 'john'
    assert setup['connection_handler_mock'].session.add.call_args[0][0].last_name == 'Doe'
    assert setup['connection_handler_mock'].session.add.call_args[0][0].pet_id == 1
    assert setup['connection_handler_mock'].session.add.call_args[0][0].age == 32

@pytest.mark.skip(reason='Database interaction')
def test_insert_person_integration():
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name='john', last_name='Doe', age=22, pet_id=1)

@pytest.mark.skip(reason='Database interaction')
def test_get_person_integration():
    repo = PeopleRepository(db_connection_handler)
    found_person = repo.get_person(3)
    print(found_person)
