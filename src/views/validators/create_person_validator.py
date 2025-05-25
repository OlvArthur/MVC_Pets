from pydantic import BaseModel, ConfigDict, ValidationError

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest

def create_person_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        first_name: str
        last_name: str
        age: int | None = None
        pet_id: int

        model_config = ConfigDict(str_min_length=1)

    try:
        BodyData(**http_request.body)
    except ValidationError as err:
        raise HttpUnprocessableEntityError(err.errors()) from err
