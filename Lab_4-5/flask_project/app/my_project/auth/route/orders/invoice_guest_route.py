from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import invoice_guest_controller
from flask_project.app.my_project.auth.domain import InvoiceGuest

invoice_guest_bp = Blueprint('invoice_guest', __name__, url_prefix='/invoice_guest')


@invoice_guest_bp.get('')
def get_all_invoice_guests() -> Response:
    return make_response(jsonify(invoice_guest_controller.find_all()), HTTPStatus.OK)


@invoice_guest_bp.post('')
def create_invoice_guest() -> Response:
    content = request.get_json()
    invoice_guest = InvoiceGuest.create_from_dto(content)
    invoice_guest_controller.create(invoice_guest)
    return make_response(jsonify(invoice_guest.put_into_dto()), HTTPStatus.CREATED)


@invoice_guest_bp.get('/<int:invoice_guest_id>')
def get_invoice_guest(invoice_guest_id: int) -> Response:
    return make_response(jsonify(invoice_guest_controller.find_by_id(invoice_guest_id)), HTTPStatus.OK)


@invoice_guest_bp.put('/<int:invoice_guest_id>')
def update_invoice_guest(invoice_guest_id: int) -> Response:
    content = request.get_json()
    invoice_guest = InvoiceGuest.create_from_dto(content)
    invoice_guest_controller.update(invoice_guest_id, invoice_guest)
    return make_response("InvoiceGuest updated", HTTPStatus.OK)


@invoice_guest_bp.patch('/<int:invoice_guest_id>')
def patch_invoice_guest(invoice_guest_id: int) -> Response:
    content = request.get_json()
    invoice_guest_controller.patch(invoice_guest_id, content)
    return make_response("InvoiceGuest updated", HTTPStatus.OK)


@invoice_guest_bp.delete('/<int:invoice_guest_id>')
def delete_invoice_guest(invoice_guest_id: int) -> Response:
    invoice_guest_controller.delete(invoice_guest_id)
    return make_response("InvoiceGuest deleted", HTTPStatus.OK)


@invoice_guest_bp.delete('')
def delete_all_invoice_guests() -> Response:
    invoice_guest_controller.delete_all()
    return make_response("All invoice guests deleted", HTTPStatus.OK)

@invoice_guest_bp.get('/get-reservation-after-guest/<int:guest_id>')
def get_reservation_after_guest(guest_id: int) -> Response:
    return make_response(jsonify(invoice_guest_controller.get_reservation_after_guest(guest_id)),
                         HTTPStatus.OK)

@invoice_guest_bp.get('/get-guest-after-reservation/<int:reservation_id>')
def get_guest_after_reservation(reservation_id: int) -> Response:
    return make_response(jsonify(invoice_guest_controller.get_guest_after_reservation(reservation_id)),
                         HTTPStatus.OK)
