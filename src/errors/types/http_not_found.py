from .http_base_exception import HttpBaseException

class HttpNotFoundError(HttpBaseException, Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message=message, status_code=404, name='NotFound')
