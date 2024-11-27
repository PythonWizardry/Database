from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import guest_controller
from flask_project.app.my_project.auth.domain import Guest

guest_bp = Blueprint('guest', __name__, url_prefix='/guest')


@guest_bp.get('')
def get_all_guest() -> Response:

    return make_response(jsonify(guest_controller.find_all()), HTTPStatus.OK)


@guest_bp.post('')
def create_guest() -> Response:

    content = request.get_json()
    guest = Guest.create_from_dto(content)
    guest_controller.create(guest)
    return make_response(jsonify(guest.put_into_dto()), HTTPStatus.CREATED)


@guest_bp.get('/<int:guest_id>')
def get_guest(guest_id: int) -> Response:

    return make_response(jsonify(guest_controller.find_by_id(guest_id)), HTTPStatus.OK)


@guest_bp.put('/<int:guest_id>')
def update_guest(guest_id: int) -> Response:

    content = request.get_json()
    guest = Guest.create_from_dto(content)
    guest_controller.update(guest_id, guest)
    return make_response("Guest updated", HTTPStatus.OK)


@guest_bp.patch('/<int:guest_id>')
def patch_guest(guest_id: int) -> Response:

    content = request.get_json()
    guest_controller.patch(guest_id, content)
    return make_response("Guest updated", HTTPStatus.OK)


@guest_bp.delete('/<int:guest_id>')
def delete_guest(guest_id: int) -> Response:

    guest_controller.delete(guest_id)
    return make_response("Guest deleted", HTTPStatus.OK)


@guest_bp.delete('')
def delete_guest_all() -> Response:
    guest_controller.delete_all()
    return make_response("All guests deleted", HTTPStatus.OK)

@guest_bp.get('/get-guest-after-address-id/<int:address_id>')
def get_guest_after_address_id(address_id: int) -> Response:
    return make_response(jsonify(guest_controller.get_guest_after_address_id(address_id)),
                         HTTPStatus.OK)