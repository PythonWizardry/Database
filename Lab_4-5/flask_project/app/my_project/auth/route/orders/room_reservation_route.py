from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import room_reservation_controller
from flask_project.app.my_project.auth.domain import RoomReservation

room_reservation_bp = Blueprint('room_reservation', __name__, url_prefix='/room_reservation')


@room_reservation_bp.get('')
def get_all_room_reservation() -> Response:

    return make_response(jsonify(room_reservation_controller.find_all()), HTTPStatus.OK)


@room_reservation_bp.post('')
def create_room_reservation() -> Response:

    content = request.get_json()
    room_reservation = RoomReservation.create_from_dto(content)
    room_reservation_controller.create(room_reservation)
    return make_response(jsonify(room_reservation.put_into_dto()), HTTPStatus.CREATED)


@room_reservation_bp.get('/<int:room_reservation_id>')
def get_room_reservation(room_reservation_id: int) -> Response:

    return make_response(jsonify(room_reservation_controller.find_by_id(room_reservation_id)), HTTPStatus.OK)


@room_reservation_bp.put('/<int:room_reservation_id>')
def update_room_reservation(room_reservation_id: int) -> Response:

    content = request.get_json()
    room_reservation = RoomReservation.create_from_dto(content)
    room_reservation_controller.update(room_reservation_id, room_reservation)
    return make_response("Room reservation updated", HTTPStatus.OK)


@room_reservation_bp.patch('/<int:room_reservation_id>')
def patch_room_reservation(room_reservation_id: int) -> Response:

    content = request.get_json()
    room_reservation_controller.patch(room_reservation_id, content)
    return make_response("Room reservation updated", HTTPStatus.OK)


@room_reservation_bp.delete('/<int:room_reservation_id>')
def delete_room_reservation(room_reservation_id: int) -> Response:

    room_reservation_controller.delete(room_reservation_id)
    return make_response("Room reservation deleted", HTTPStatus.OK)


@room_reservation_bp.delete('')
def delete_room_reservation_all() -> Response:
    room_reservation_controller.delete_all()
    return make_response("All room reservations deleted", HTTPStatus.OK)

@room_reservation_bp.get('/get-room-after-reservation/<int:reservation_id>')
def get_room_after_reservation(reservation_id: int) -> Response:
    return make_response(jsonify(room_reservation_controller.get_room_after_reservation(reservation_id)),
                         HTTPStatus.OK)

@room_reservation_bp.get('/get-reservation-after-room/<int:room_id>')
def get_reservation_after_room(room_id: int) -> Response:
    return make_response(jsonify(room_reservation_controller.get_reservation_after_room(room_id)),
                         HTTPStatus.OK)


@room_reservation_bp.post('/insert-into-room-reservation')
def create_into_room_reservation() -> Response:
    content = request.get_json()
    room_name = content['room_name']
    reservation_created = content['reservation_created']
    discount_percent = content['discount_percent']
    total_price = content['total_price']
    room_reservation_controller.insert_into_room_reservation(room_name, reservation_created, discount_percent, total_price)
    return make_response(jsonify(room_reservation_controller.find_all()), HTTPStatus.CREATED)
