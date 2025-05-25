from flask import Blueprint, jsonify
from src.main.composer.delete_pet_composer import delete_pet_composer
from src.main.composer.list_pets_composer import list_pets_composer
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors


pet_routes_bp = Blueprint("pets_routes", __name__)

@pet_routes_bp.route('/pets', methods=['GET'])
def list_pets():
    try:
        view = list_pets_composer()
        http_request = HttpRequest()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code



@pet_routes_bp.route('/pets/<name>', methods=['DELETE'])
def delete_pet(name):
    try:
        http_request = HttpRequest(params={'name': name})
        view = delete_pet_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exc:
        http_response = handle_errors(exc)
        return jsonify(http_response.body), http_response.status_code
