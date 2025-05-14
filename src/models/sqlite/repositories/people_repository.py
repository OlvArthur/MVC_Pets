from sqlalchemy.exc import NoResultFound
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.entities.pets import PetsTable
from src.models.interfaces.repositories.people_repository import PeopleRepositoryInterface

class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int ) -> None:
        with self.__db_connection as database:
            try:
                new_person = (
                    PeopleTable(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
                )

                database.session.add(new_person)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    def get_person(self, person_id: int) -> PeopleTable | None:
        with self.__db_connection as database:
            try:
                found_person = (
                    database.session
                        .query(PeopleTable)
                        .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                        .filter(PeopleTable.id == person_id)
                        .with_entities(
                            PeopleTable.first_name,
                            PeopleTable.last_name,
                            PetsTable.name.label('pet_name'),
                            PetsTable.type.label('pet_type'),
                        ).one()
                )
                return found_person
            except NoResultFound:
                return None
