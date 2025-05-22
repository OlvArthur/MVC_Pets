from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controllers.create_person_controller import CreatePersonController
from src.views.create_person_view import CreatePersonView

def create_person_composer():
    model = PeopleRepository(db_connection_handler)
    controller = CreatePersonController(model)
    view = CreatePersonView(controller)

    return view
