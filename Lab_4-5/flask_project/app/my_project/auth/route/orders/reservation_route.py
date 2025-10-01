from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import reservation_controller
from flask_project.app.my_project.auth.domain import Reservation

reservation_bp = Blueprint('reservation', __name__, url_prefix='/reservation')


@reservation_bp.get('')
def get_all_reservation() -> Response:
    """
    Get all reservations
    ---
    responses:
      200:
        description: Returns a list of reservations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(reservation_controller.find_all()), HTTPStatus.OK)


@reservation_bp.post('')
def create_reservation() -> Response:
    """
    Create a new reservation
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
            status_id:
              type: integer
              description: Status ID
            start_date:
              type: string
              format: date
              description: Start date (YYYY-MM-DD)
            end_date:
              type: string
              format: date
              description: End date (YYYY-MM-DD)
            ts_created:
              type: string
              format: date-time
              description: Timestamp created
            ts_updated:
              type: string
              format: date-time
              description: Timestamp updated
          required:
            - guest_id
            - status_id
            - start_date
            - end_date
            - ts_created
            - ts_updated
    responses:
      201:
        description: Returns the created reservation
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.create(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)


@reservation_bp.get('/<int:reservation_id>')
def get_reservation(reservation_id: int) -> Response:
    """
    Get a reservation by ID
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
        description: Returns the reservation
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(reservation_controller.find_by_id(reservation_id)), HTTPStatus.OK)


@reservation_bp.put('/<int:reservation_id>')
def update_reservation(reservation_id: int) -> Response:
    """
    Update a reservation by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the reservation
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            guest_id:
              type: integer
            status_id:
              type: integer
            start_date:
              type: string
              format: date
            end_date:
              type: string
              format: date
            ts_created:
              type: string
              format: date-time
            ts_updated:
              type: string
              format: date-time
          required:
            - guest_id
            - status_id
            - start_date
            - end_date
            - ts_created
            - ts_updated
    responses:
      200:
        description: Reservation updated
    """
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.update(reservation_id, reservation)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservation_bp.patch('/<int:reservation_id>')
def patch_reservation(reservation_id: int) -> Response:
    """
    Patch a reservation by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the reservation
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Reservation updated
    """
    content = request.get_json()
    reservation_controller.patch(reservation_id, content)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservation_bp.delete('/<int:reservation_id>')
def delete_reservation(reservation_id: int) -> Response:
    """
    Delete a reservation by ID
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
        description: Reservation deleted
    """
    reservation_controller.delete(reservation_id)
    return make_response("Reservation deleted", HTTPStatus.OK)


@reservation_bp.delete('')
def delete_reservation_all() -> Response:
    """
    Delete all reservations
    ---
    responses:
      200:
        description: All reservations deleted
    """
    reservation_controller.delete(reservation_controller.find_all())
    return make_response("All Reservation deleted", HTTPStatus.OK)

@reservation_bp.get('/get-reservation-after-guest-id/<int:guest_id>')
def get_reservation_after_guest_id(guest_id: int) -> Response:
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
    return make_response(jsonify(reservation_controller.get_reservation_after_guest_id(guest_id)),
                         HTTPStatus.OK)

@reservation_bp.get('/get-reservation-after-status-id/<int:status_id>')
def get_reservation_after_status_id(status_id: int) -> Response:
    """
    Get reservations by status ID
    ---
    parameters:
      - in: path
        name: status_id
        required: true
        schema:
          type: integer
        description: The ID of the status
    responses:
      200:
        description: Returns reservations for the given status ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(reservation_controller.get_reservation_after_status_id(status_id)),
                         HTTPStatus.OK)
