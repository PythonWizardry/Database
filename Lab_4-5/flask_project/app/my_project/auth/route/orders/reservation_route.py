from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import reservation_controller
from flask_project.app.my_project.auth.domain import Reservation

reservation_bp = Blueprint('reservation', __name__, url_prefix='/reservation')


@reservation_bp.get('')
def get_all_reservation() -> Response:
    return make_response(jsonify(reservation_controller.find_all()), HTTPStatus.OK)


@reservation_bp.post('')
def create_reservation() -> Response:
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.create(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)


@reservation_bp.get('/<int:reservation_id>')
def get_reservation(reservation_id: int) -> Response:
    return make_response(jsonify(reservation_controller.find_by_id(reservation_id)), HTTPStatus.OK)


@reservation_bp.put('/<int:reservation_id>')
def update_reservation(reservation_id: int) -> Response:
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.update(reservation_id, reservation)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservation_bp.patch('/<int:reservation_id>')
def patch_reservation(reservation_id: int) -> Response:
    content = request.get_json()
    reservation_controller.patch(reservation_id, content)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservation_bp.delete('/<int:reservation_id>')
def delete_reservation(reservation_id: int) -> Response:
    reservation_controller.delete(reservation_id)
    return make_response("Reservation deleted", HTTPStatus.OK)


@reservation_bp.delete('')
def delete_reservation_all() -> Response:
    reservation_controller.delete(reservation_controller.find_all())
    return make_response("All Reservation deleted", HTTPStatus.OK)

@reservation_bp.get('/get-reservation-after-guest-id/<int:guest_id>')
def get_reservation_after_guest_id(guest_id: int) -> Response:
    return make_response(jsonify(reservation_controller.get_reservation_after_guest_id(guest_id)),
                         HTTPStatus.OK)

@reservation_bp.get('/get-reservation-after-status-id/<int:status_id>')
def get_reservation_after_status_id(status_id: int) -> Response:
    return make_response(jsonify(reservation_controller.get_reservation_after_status_id(status_id)),
                         HTTPStatus.OK)
