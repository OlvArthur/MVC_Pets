from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.people import PeopleTable

class PeopleRepository:
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
