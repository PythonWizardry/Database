from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import room_controller
from flask_project.app.my_project.auth.domain import Room

room_bp = Blueprint('room', __name__, url_prefix='/room')


@room_bp.get('')
def get_all_room() -> Response:
    """
    Get all rooms
    ---
    tags:
      - Room
    responses:
      200:
        description: Returns a list of rooms
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(room_controller.find_all()), HTTPStatus.OK)


@room_bp.post('')
def create_room() -> Response:
    """
    Create a new room
    ---
    tags:
      - Room
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The room name
            description:
              type: string
              description: Room description
            price:
              type: number
              format: float
              description: Room price
            hotel_id:
              type: integer
              description: Hotel ID
            status_id:
              type: integer
              description: Status ID
            type_id:
              type: integer
              description: Type ID
          required:
            - name
            - price
            - hotel_id
            - status_id
            - type_id
    responses:
      201:
        description: Returns the created room
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.create(room)
    return make_response(jsonify(room.put_into_dto()), HTTPStatus.CREATED)


@room_bp.get('/<int:room_id>')
def get_room(room_id: int) -> Response:
    """
    Get a room by ID
    ---
    tags:
      - Room
    parameters:
      - in: path
        name: room_id
        required: true
        schema:
          type: integer
        description: The ID of the room
    responses:
      200:
        description: Returns the room
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(room_controller.find_by_id(room_id)), HTTPStatus.OK)


@room_bp.put('/<int:room_id>')
def update_room(room_id: int) -> Response:
    """
    Update a room by ID
    ---
    tags:
      - Room
    consumes:
      - application/json
    parameters:
      - in: path
        name: room_id
        required: true
        schema:
          type: integer
        description: The ID of the room
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
            price:
              type: number
              format: float
            hotel_id:
              type: integer
            status_id:
              type: integer
            type_id:
              type: integer
          required:
            - name
            - price
            - hotel_id
            - status_id
            - type_id
    responses:
      200:
        description: Room updated
    """
    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.update(room_id, room)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.patch('/<int:room_id>')
def patch_room(room_id: int) -> Response:
    """
    Patch a room by ID
    ---
    tags:
      - Room
    consumes:
      - application/json
    parameters:
      - in: path
        name: room_id
        required: true
        schema:
          type: integer
        description: The ID of the room
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Room updated
    """
    content = request.get_json()
    room_controller.patch(room_id, content)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.delete('/<int:room_id>')
def delete_room(room_id: int) -> Response:
    """
    Delete a room by ID
    ---
    tags:
      - Room
    parameters:
      - in: path
        name: room_id
        required: true
        schema:
          type: integer
        description: The ID of the room
    responses:
      200:
        description: Room deleted
    """
    room_controller.delete(room_id)
    return make_response("Room deleted", HTTPStatus.OK)


@room_bp.delete('')
def delete_room_all() -> Response:
    """
    Delete all rooms
    ---
    tags:
      - Room
    responses:
      200:
        description: All rooms deleted
    """
    room_controller.delete_all()
    return make_response("All rooms deleted", HTTPStatus.OK)

@room_bp.get('/get-room-after-status-id/<int:status_id>')
def get_room_after_status_id(status_id: int) -> Response:
    """
    Get rooms by status ID
    ---
    tags:
      - Room
    parameters:
      - in: path
        name: status_id
        required: true
        schema:
          type: integer
        description: The ID of the status
    responses:
      200:
        description: Returns rooms with the given status ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(room_controller.get_room_after_status_id(status_id)),
                         HTTPStatus.OK)

@room_bp.get('/get-room-after-hotel-id/<int:hotel_id>')
def get_room_after_hotel_id(hotel_id: int) -> Response:
    """
    Get rooms by hotel ID
    ---
    tags:
      - Room
    parameters:
      - in: path
        name: hotel_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel
    responses:
      200:
        description: Returns rooms with the given hotel ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(room_controller.get_room_after_hotel_id(hotel_id)),
                         HTTPStatus.OK)

@room_bp.get('/get-room-after-type-id/<int:type_id>')
def get_room_after_type_id(type_id: int) -> Response:
    """
    Get rooms by type ID
    ---
    tags:
      - Room
    parameters:
      - in: path
        name: type_id
        required: true
        schema:
          type: integer
        description: The ID of the type
    responses:
      200:
        description: Returns rooms with the given type ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(room_controller.get_room_after_type_id(type_id)),
                         HTTPStatus.OK)