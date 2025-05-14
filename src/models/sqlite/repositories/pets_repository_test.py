from unittest import mock
from typing import TypedDict
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.exc import NoResultFound

from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.pets import PetsTable
from src.models.interfaces.entities.pets import PetsInterface

from .pets_repository import PetsRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Database interaction')
def test_list_pets_integration():
    repo = PetsRepository(db_connection_handler)
    pets = repo.list_pets()

    assert len(pets) != 0

@pytest.mark.skip(reason='Database interaction')
def test_delete_pet_integration():
    pet_name = 'belinha'

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(pet_name)


class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(data=[
            (
                [
                    mock.call.query(PetsTable)
                ],
                [
                    PetsTable(name='cobra', type='snake'),
                    PetsTable(name='cao', type='dog'),
                    PetsTable(name='belinha',type='dog'),
                    PetsTable(name='burro',type='donkey')
                ]
            ),
            (
                [
                    mock.call.query(PetsTable),
                    mock.call.filter(PetsTable.name == 'shrek')
                ],
                [
                    PetsTable(name='shrek', type='dog')
                ]
            )
        ])

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

class NoDataConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_result_not_found

    def __raise_result_not_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

class SetupVariables(TypedDict):
    repo: PetsRepository
    connection_handler_mock: ConnectionHandlerMock
    no_data_repo: PetsRepository
    no_data_connection_handler_mock: NoDataConnectionHandlerMock

@pytest.fixture
def setup() -> SetupVariables:  # type: ignore
    db_connection_handler_mock = ConnectionHandlerMock()
    repo = PetsRepository(db_connection_handler_mock)

    no_data_db_connection_handler_mock = NoDataConnectionHandlerMock()
    no_data_repo = PetsRepository(no_data_db_connection_handler_mock)
    setup_variables = {
        'repo': repo,
        'connection_handler_mock': db_connection_handler_mock,
        'no_data_repo': no_data_repo,
        'no_data_connection_handler_mock': no_data_db_connection_handler_mock
    }

    yield setup_variables

def test_list_pets(setup):
    pets = setup['repo'].list_pets()

    setup['connection_handler_mock'].session.query.assert_called_once_with(PetsTable)
    setup['connection_handler_mock'].session.all.assert_called_once()
    setup['connection_handler_mock'].session.filter.assert_not_called()

    assert len(pets) == 4


def test_delete_pet(setup):
    pet_name = 'shrek'

    setup['repo'].delete_pets(pet_name)

    setup['connection_handler_mock'].session.query.assert_called_once_with(PetsTable)
    (setup['connection_handler_mock'].session
            .filter.assert_called_once_with(PetsTable.name == pet_name))
    setup['connection_handler_mock'].session.delete.assert_called_once()
    setup['connection_handler_mock'].session.commit.assert_called_once()


def test_list_pets_no_result(setup):
    pets = setup['no_data_repo'].list_pets()

    setup['no_data_connection_handler_mock'].session.query.assert_called_once_with(PetsTable)
    setup['no_data_connection_handler_mock'].session.all.assert_not_called()

    assert pets == []

def test_delete_pet_error(setup):
    with pytest.raises(Exception):
        setup['no_data_repo'].delete_pets('zeca')

    setup['no_data_connection_handler_mock'].session.rollback.assert_called_once()

def test_entity_interface_implementation():
    assert isinstance(PetsTable(), PetsInterface)
