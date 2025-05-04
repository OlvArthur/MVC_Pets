from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.settings.connection import DBConnectionHandler
from src.models.sqlite.entities.pets import PetsTable

class PetsRepository:
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> list[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, pet_name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(PetsTable)
                        .filter(PetsTable.name == pet_name)
                        .delete()
                )
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc
