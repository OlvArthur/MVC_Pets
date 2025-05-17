from unittest import mock
import pytest

from .delete_pet_controller import DeletePetController

class PetRepositoryMock:
    def delete_pets(self, pet_name: str) -> None: pass

def test_delete_pet():
    repo_mock = mock.Mock()
    controller = DeletePetController(repo_mock)

    controller.execute('belinha')

    repo_mock.delete_pets.assert_called_once_with('belinha')


def test_invalid_pet_name():
    repo_mock = PetRepositoryMock()
    controller = DeletePetController(repo_mock)

    with pytest.raises(Exception) as exc:
        controller.execute(34)

    assert str(exc.value) == 'Invalid Pet name'
