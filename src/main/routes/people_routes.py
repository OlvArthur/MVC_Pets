from flask import Blueprint, request, jsonify

from src.main.composer.create_person_composer import create_person_composer
from src.main.composer.find_person_composer import find_person_composer
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors


people_routes_bp = Blueprint('people_routes', __name__)

@people_routes_bp.route('/people', methods=['POST'])
def create_person():
    try:
        view = create_person_composer()

        http_request = HttpRequest(body=request.json)
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(error=exc)
        return jsonify(http_response.body), http_response.status_code



@people_routes_bp.route('/people/<id>', methods=['GET'])
def find_person(id):
    try:
        http_request = HttpRequest(params={'id': int(id)})
        view = find_person_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        print(exc)
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code
