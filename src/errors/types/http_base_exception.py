from src.errors.interfaces.base_exception import BaseExceptionInterface
from src.views.http_types.http_response import HttpResponse

class HttpBaseException(BaseExceptionInterface, Exception):
    def __init__(self, status_code: int, name: str, message: str):
        super().__init__(message)
        self.status_code = status_code
        self.name = name
        self.message = message

    def handle(self) -> HttpResponse:
        return HttpResponse(
            status_code=self.status_code,
            body={
                "error": {
                    "title": self.name,
                    "detail": self.message
                }
            }
        )
