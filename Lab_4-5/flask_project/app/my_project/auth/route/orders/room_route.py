from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import room_controller
from flask_project.app.my_project.auth.domain import Room

room_bp = Blueprint('room', __name__, url_prefix='/room')


@room_bp.get('')
def get_all_room() -> Response:

    return make_response(jsonify(room_controller.find_all()), HTTPStatus.OK)


@room_bp.post('')
def create_room() -> Response:

    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.create(room)
    return make_response(jsonify(room.put_into_dto()), HTTPStatus.CREATED)


@room_bp.get('/<int:room_id>')
def get_room(room_id: int) -> Response:

    return make_response(jsonify(room_controller.find_by_id(room_id)), HTTPStatus.OK)


@room_bp.put('/<int:room_id>')
def update_room(room_id: int) -> Response:

    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.update(room_id, room)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.patch('/<int:room_id>')
def patch_room(room_id: int) -> Response:

    content = request.get_json()
    room_controller.patch(room_id, content)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.delete('/<int:room_id>')
def delete_room(room_id: int) -> Response:

    room_controller.delete(room_id)
    return make_response("Room deleted", HTTPStatus.OK)


@room_bp.delete('')
def delete_room_all() -> Response:
    room_controller.delete_all()
    return make_response("All rooms deleted", HTTPStatus.OK)

@room_bp.get('/get-room-after-status-id/<int:status_id>')
def get_room_after_status_id(status_id: int) -> Response:
    return make_response(jsonify(room_controller.get_room_after_status_id(status_id)),
                         HTTPStatus.OK)

@room_bp.get('/get-room-after-hotel-id/<int:hotel_id>')
def get_room_after_hotel_id(hotel_id: int) -> Response:
    return make_response(jsonify(room_controller.get_room_after_hotel_id(hotel_id)),
                         HTTPStatus.OK)

@room_bp.get('/get-room-after-type-id/<int:type_id>')
def get_room_after_type_id(type_id: int) -> Response:
    return make_response(jsonify(room_controller.get_room_after_type_id(type_id)),
                         HTTPStatus.OK)