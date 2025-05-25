from abc import ABC, abstractmethod
from src.views.http_types.http_response import HttpResponse

class BaseExceptionInterface(ABC):
    @abstractmethod
    def handle(self) -> HttpResponse: pass
        