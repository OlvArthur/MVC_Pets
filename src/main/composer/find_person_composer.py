from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.find_person_controller import FindPersonController
from src.views.find_person_view import FindPersonView

def find_person_composer():
    model = PeopleRepository(db_connection_handler)
    controller = FindPersonController(model)
    view = FindPersonView(controller)

    return view
