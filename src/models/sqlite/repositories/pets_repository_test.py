from unittest import mock
import pytest

from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.entities.pets import PetsTable
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
                    mock.call.query(PetsTable),
                ],
                [
                    PetsTable(name='cobra', type='snake'),
                    PetsTable(name='cao', type='dog'),
                    PetsTable(name='belinha',type='dog'),
                    PetsTable(name='burro',type='donkey')
                ]
            )
        ])

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass


def test_list_pets():
    db_connection_handler_mock = ConnectionHandlerMock()
    repo = PetsRepository(db_connection_handler_mock)
    pets = repo.list_pets()

    db_connection_handler_mock.session.query.assert_called_once_with(PetsTable)
    db_connection_handler_mock.session.all.assert_called_once()
    db_connection_handler_mock.session.filter.assert_not_called()

    assert len(pets) == 4
