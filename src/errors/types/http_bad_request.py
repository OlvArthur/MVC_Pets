from .http_base_exception import HttpBaseException

class HttpBadRequestError(HttpBaseException, Exception):
    def __init__(self, message: str):
        super().__init__(message=message,status_code=400, name='BadRequest')
