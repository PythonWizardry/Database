from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import room_reservation_controller
from flask_project.app.my_project.auth.domain import RoomReservation

room_reservation_bp = Blueprint('room_reservation', __name__, url_prefix='/room_reservation')


@room_reservation_bp.get('')
def get_all_room_reservation() -> Response:
    """
    Get all room reservations
    ---
    tags:
      - RoomReservation
    responses:
      200:
        description: Returns a list of room reservations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(room_reservation_controller.find_all()), HTTPStatus.OK)


@room_reservation_bp.post('')
def create_room_reservation() -> Response:
    """
    Create a new room reservation
    ---
    tags:
      - RoomReservation
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            room_id:
              type: integer
              description: Room ID
            reservation_id:
              type: integer
              description: Reservation ID
            discount_percent:
              type: number
              format: float
              description: Discount percent
            total_price:
              type: number
              format: float
              description: Total price
          required:
            - room_id
            - reservation_id
            - total_price
    responses:
      201:
        description: Returns the created room reservation
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    room_reservation = RoomReservation.create_from_dto(content)
    room_reservation_controller.create(room_reservation)
    return make_response(jsonify(room_reservation.put_into_dto()), HTTPStatus.CREATED)


@room_reservation_bp.get('/<int:room_reservation_id>')
def get_room_reservation(room_reservation_id: int) -> Response:
    """
    Get a room reservation by ID
    ---
    tags:
      - RoomReservation
    parameters:
      - in: path
        name: room_reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the room reservation
    responses:
      200:
        description: Returns the room reservation
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(room_reservation_controller.find_by_id(room_reservation_id)), HTTPStatus.OK)


@room_reservation_bp.put('/<int:room_reservation_id>')
def update_room_reservation(room_reservation_id: int) -> Response:
    """
    Update a room reservation by ID
    ---
    tags:
      - RoomReservation
    consumes:
      - application/json
    parameters:
      - in: path
        name: room_reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the room reservation
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            room_id:
              type: integer
            reservation_id:
              type: integer
            discount_percent:
              type: number
              format: float
            total_price:
              type: number
              format: float
          required:
            - room_id
            - reservation_id
            - total_price
    responses:
      200:
        description: Room reservation updated
    """
    content = request.get_json()
    room_reservation = RoomReservation.create_from_dto(content)
    room_reservation_controller.update(room_reservation_id, room_reservation)
    return make_response("Room reservation updated", HTTPStatus.OK)


@room_reservation_bp.patch('/<int:room_reservation_id>')
def patch_room_reservation(room_reservation_id: int) -> Response:
    """
    Patch a room reservation by ID
    ---
    tags:
      - RoomReservation
    consumes:
      - application/json
    parameters:
      - in: path
        name: room_reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the room reservation
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Room reservation updated
    """
    content = request.get_json()
    room_reservation_controller.patch(room_reservation_id, content)
    return make_response("Room reservation updated", HTTPStatus.OK)


@room_reservation_bp.delete('/<int:room_reservation_id>')
def delete_room_reservation(room_reservation_id: int) -> Response:
    """
    Delete a room reservation by ID
    ---
    tags:
      - RoomReservation
    parameters:
      - in: path
        name: room_reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the room reservation
    responses:
      200:
        description: Room reservation deleted
    """
    room_reservation_controller.delete(room_reservation_id)
    return make_response("Room reservation deleted", HTTPStatus.OK)


@room_reservation_bp.delete('')
def delete_room_reservation_all() -> Response:
    """
    Delete all room reservations
    ---
    tags:
      - RoomReservation
    responses:
      200:
        description: All room reservations deleted
    """
    room_reservation_controller.delete_all()
    return make_response("All room reservations deleted", HTTPStatus.OK)

@room_reservation_bp.get('/get-room-after-reservation/<int:reservation_id>')
def get_room_after_reservation(reservation_id: int) -> Response:
    """
    Get rooms by reservation ID
    ---
    tags:
      - RoomReservation
    parameters:
      - in: path
        name: reservation_id
        required: true
        schema:
          type: integer
        description: The ID of the reservation
    responses:
      200:
        description: Returns rooms for the given reservation ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(room_reservation_controller.get_room_after_reservation(reservation_id)),
                         HTTPStatus.OK)

@room_reservation_bp.get('/get-reservation-after-room/<int:room_id>')
def get_reservation_after_room(room_id: int) -> Response:
    """
    Get reservations by room ID
    ---
    tags:
      - RoomReservation
    parameters:
      - in: path
        name: room_id
        required: true
        schema:
          type: integer
        description: The ID of the room
    responses:
      200:
        description: Returns reservations for the given room ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
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
