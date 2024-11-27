from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import city_controller
from flask_project.app.my_project.auth.domain import City

city_bp = Blueprint('city', __name__, url_prefix='/city')


@city_bp.get('')
def get_all_cities() -> Response:
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)


@city_bp.post('')
def create_city() -> Response:
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.CREATED)


@city_bp.get('/<int:city_id>')
def get_city(city_id: int) -> Response:
    return make_response(jsonify(city_controller.find_by_id(city_id)), HTTPStatus.OK)


@city_bp.put('/<int:city_id>')
def update_city(city_id: int) -> Response:
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.update(city_id, city)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.patch('/<int:city_id>')
def patch_city(city_id: int) -> Response:
    content = request.get_json()
    city_controller.patch(city_id, content)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.delete('/<int:city_id>')
def delete_city(city_id: int) -> Response:
    city_controller.delete(city_id)
    return make_response("City deleted", HTTPStatus.OK)


@city_bp.delete('')
def delete_all_cities() -> Response:
    city_controller.delete_all()
    return make_response("All cities deleted", HTTPStatus.OK)

@city_bp.post('/package-insert')
def create_packages() -> Response:
    city_controller.package_insert()
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.CREATED)
