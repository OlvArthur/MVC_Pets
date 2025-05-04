import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Database interaction')
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    pets = repo.list_pets()

    print(pets)
    assert len(pets) != 0

@pytest.mark.skip(reason='Database interaction')
def test_delete_pet():
    pet_name = 'belinha'

    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(pet_name)
