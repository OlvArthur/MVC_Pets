from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.__engine: Engine | None = None
        self.session: Session | None = None


    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)


    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = DBConnectionHandler()
