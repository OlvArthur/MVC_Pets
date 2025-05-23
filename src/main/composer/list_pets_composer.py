from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.controllers.list_pets_controller import ListPetsController
from src.views.list_pets_view import ListPetsView

def list_pets_composer():
    model = PetsRepository(db_connection_handler)
    controller = ListPetsController(model)
    view = ListPetsView(controller)

    return view
