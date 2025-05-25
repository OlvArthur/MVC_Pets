from pydantic import BaseModel, ConfigDict, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def delete_pet_validator(http_request: HttpRequest) -> None:
    class ParamsData(BaseModel):
        name: str

        model_config = ConfigDict(str_min_length=1)

    try:
        ParamsData(**http_request.params)

    except ValidationError as exc:
        raise HttpUnprocessableEntityError(exc.errors()) from exc
