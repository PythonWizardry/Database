from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import address_controller
from flask_project.app.my_project.auth.domain import Address

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.get('')
def get_all_address() -> Response:

    return make_response(jsonify(address_controller.find_all()), HTTPStatus.OK)


@address_bp.post('')
def create_address() -> Response:

    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.get('/<int:address_id>')
def get_address(address_id: int) -> Response:

    return make_response(jsonify(address_controller.find_by_id(address_id)), HTTPStatus.OK)


@address_bp.put('/<int:address_id>')
def update_address(address_id: int) -> Response:

    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update(address_id, address)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.patch('/<int:address_id>')
def patch_address(address_id: int) -> Response:

    content = request.get_json()
    address_controller.patch(address_id, content)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.delete('/<int:address_id>')
def delete_address(address_id: int) -> Response:

    address_controller.delete(address_id)
    return make_response("Address deleted", HTTPStatus.OK)



