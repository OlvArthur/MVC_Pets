from sqlalchemy import create_engine, Engine

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.__engine: Engine = None


    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)


    def get_engine(self):
        return self.__engine


db_connection_handler = DBConnectionHandler()
