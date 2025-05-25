from src.views.http_types.http_response import HttpResponse
from src.errors.interfaces.base_exception import BaseExceptionInterface

def handle_errors(error: Exception) -> HttpResponse:
    if not isinstance (error, BaseExceptionInterface):
        return HttpResponse(
            status_code='500',
            body={
                'error': {
                    'title': 'Server Error',
                    'detail': str(error)
                }
            }
        )

    response = error.handle()

    return response
