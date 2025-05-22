from flask import Blueprint, request, jsonify
from src.main.composer.create_person_composer import create_person_composer
from src.views.http_types.http_request import HttpRequest


people_routes_bp = Blueprint('people_routes', __name__)

@people_routes_bp.route('/people', methods=['POST'])
def create_person():
    view = create_person_composer()

    http_request = HttpRequest(body=request.json)
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
