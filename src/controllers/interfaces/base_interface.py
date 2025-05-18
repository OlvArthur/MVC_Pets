from abc import ABC, abstractmethod
from typing import TypedDict, NotRequired

class FormattedResponseData(TypedDict):
    type: str
    count: int
    attributes: NotRequired[dict | list[dict]]

class FormattedResponse(TypedDict):
    data: FormattedResponseData


class BaseControllerInterface(ABC):

    @abstractmethod
    def execute(self) -> FormattedResponse: pass
