from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import invoice_guest_controller
from flask_project.app.my_project.auth.domain import InvoiceGuest

invoice_guest_bp = Blueprint('invoice_guest', __name__, url_prefix='/invoice_guest')


@invoice_guest_bp.get('')
def get_all_invoice_guests() -> Response:
    """
    Get all invoice guests
    ---
    responses:
      200:
        description: Returns a list of invoice guests
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(invoice_guest_controller.find_all()), HTTPStatus.OK)


@invoice_guest_bp.post('')
def create_invoice_guest() -> Response:
    """
    Create a new invoice guest
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            guest_id:
              type: integer
              description: Guest ID
            reservation_id:
              type: integer
              description: Reservation ID
            amount:
              type: number
              format: float
              description: Invoice amount
            ts_issued:
              type: string
              format: date-time
              description: Timestamp issued
          required:
            - guest_id
            - reservation_id
            - amount
            - ts_issued
    responses:
      201:
        description: Returns the created invoice guest
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    invoice_guest = InvoiceGuest.create_from_dto(content)
    invoice_guest_controller.create(invoice_guest)
    return make_response(jsonify(invoice_guest.put_into_dto()), HTTPStatus.CREATED)


@invoice_guest_bp.get('/<int:invoice_guest_id>')
def get_invoice_guest(invoice_guest_id: int) -> Response:
    """
    Get an invoice guest by ID
    ---
    parameters:
      - in: path
        name: invoice_guest_id
        required: true
        schema:
          type: integer
        description: The ID of the invoice guest
    responses:
      200:
        description: Returns the invoice guest
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(invoice_guest_controller.find_by_id(invoice_guest_id)), HTTPStatus.OK)


@invoice_guest_bp.put('/<int:invoice_guest_id>')
def update_invoice_guest(invoice_guest_id: int) -> Response:
    """
    Update an invoice guest by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: invoice_guest_id
        required: true
        schema:
          type: integer
        description: The ID of the invoice guest
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            guest_id:
              type: integer
            reservation_id:
              type: integer
            amount:
              type: number
              format: float
            ts_issued:
              type: string
              format: date-time
          required:
            - guest_id
            - reservation_id
            - amount
            - ts_issued
    responses:
      200:
        description: Invoice guest updated
    """
    content = request.get_json()
    invoice_guest = InvoiceGuest.create_from_dto(content)
    invoice_guest_controller.update(invoice_guest_id, invoice_guest)
    return make_response("InvoiceGuest updated", HTTPStatus.OK)


@invoice_guest_bp.patch('/<int:invoice_guest_id>')
def patch_invoice_guest(invoice_guest_id: int) -> Response:
    """
    Patch an invoice guest by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: invoice_guest_id
        required: true
        schema:
          type: integer
        description: The ID of the invoice guest
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Invoice guest updated
    """
    content = request.get_json()
    invoice_guest_controller.patch(invoice_guest_id, content)
    return make_response("InvoiceGuest updated", HTTPStatus.OK)


@invoice_guest_bp.delete('/<int:invoice_guest_id>')
def delete_invoice_guest(invoice_guest_id: int) -> Response:
    """
    Delete an invoice guest by ID
    ---
    parameters:
      - in: path
        name: invoice_guest_id
        required: true
        schema:
          type: integer
        description: The ID of the invoice guest
    responses:
      200:
        description: Invoice guest deleted
    """
    invoice_guest_controller.delete(invoice_guest_id)
    return make_response("InvoiceGuest deleted", HTTPStatus.OK)


@invoice_guest_bp.delete('')
def delete_all_invoice_guests() -> Response:
    """
    Delete all invoice guests
    ---
    responses:
      200:
        description: All invoice guests deleted
    """
    invoice_guest_controller.delete_all()
    return make_response("All invoice guests deleted", HTTPStatus.OK)

@invoice_guest_bp.get('/get-reservation-after-guest/<int:guest_id>')
def get_reservation_after_guest(guest_id: int) -> Response:
    """
    Get reservations by guest ID
    ---
    parameters:
      - in: path
        name: guest_id
        required: true
        schema:
          type: integer
        description: The ID of the guest
    responses:
      200:
        description: Returns reservations for the given guest ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(invoice_guest_controller.get_reservation_after_guest(guest_id)),
                         HTTPStatus.OK)

@invoice_guest_bp.get('/get-guest-after-reservation/<int:reservation_id>')
def get_guest_after_reservation(reservation_id: int) -> Response:
    """
    Get guest by reservation ID
    ---
    parameters:
      - in: path
        name: reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the reservation
    responses:
      200:
        description: Returns guest for the given reservation ID
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(invoice_guest_controller.get_guest_after_reservation(reservation_id)),
                         HTTPStatus.OK)
