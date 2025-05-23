from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.delete_pet_controller import DeletePetController
from src.views.delete_pet_view import DeletePetView

def delete_pet_composer():
    model = PetsRepository(db_connection_handler)
    controller = DeletePetController(model)
    view = DeletePetView(controller)

    return view
