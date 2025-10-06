from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import guest_controller
from flask_project.app.my_project.auth.domain import Guest

guest_bp = Blueprint('guest', __name__, url_prefix='/guest')


@guest_bp.get('')
def get_all_guest() -> Response:
    """
    Get all guests
    ---
    tags:
      - Guest
    responses:
      200:
        description: Returns a list of guests
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(guest_controller.find_all()), HTTPStatus.OK)


@guest_bp.post('')
def create_guest() -> Response:
    """
    Create a new guest
    ---
    tags:
      - Guest
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
              description: The guest's first name
            surname:
              type: string
              description: The guest's last name
            email:
              type: string
              description: The guest's email
            phone:
              type: string
              description: The guest's phone number
            details:
              type: string
              description: Additional details
            address_id:
              type: integer
              description: Address ID
          required:
            - name
            - surname
            - email
            - phone
            - address_id
    responses:
      201:
        description: Returns the created guest
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    guest = Guest.create_from_dto(content)
    guest_controller.create(guest)
    return make_response(jsonify(guest.put_into_dto()), HTTPStatus.CREATED)


@guest_bp.get('/<int:guest_id>')
def get_guest(guest_id: int) -> Response:
    """
    Get a guest by ID
    ---
    tags:
      - Guest
    parameters:
      - in: path
        name: guest_id
        required: true
        schema:
          type: integer
        description: The ID of the guest
    responses:
      200:
        description: Returns the guest
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(guest_controller.find_by_id(guest_id)), HTTPStatus.OK)


@guest_bp.put('/<int:guest_id>')
def update_guest(guest_id: int) -> Response:
    """
    Update a guest by ID
    ---
    tags:
      - Guest
    consumes:
      - application/json
    parameters:
      - in: path
        name: guest_id
        required: true
        schema:
          type: integer
        description: The ID of the guest
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            surname:
              type: string
            email:
              type: string
            phone:
              type: string
            details:
              type: string
            address_id:
              type: integer
          required:
            - name
            - surname
            - email
            - phone
            - address_id
    responses:
      200:
        description: Guest updated
    """
    content = request.get_json()
    guest = Guest.create_from_dto(content)
    guest_controller.update(guest_id, guest)
    return make_response("Guest updated", HTTPStatus.OK)


@guest_bp.patch('/<int:guest_id>')
def patch_guest(guest_id: int) -> Response:
    """
    Patch a guest by ID
    ---
    tags:
      - Guest
    consumes:
      - application/json
    parameters:
      - in: path
        name: guest_id
        required: true
        schema:
          type: integer
        description: The ID of the guest
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Guest updated
    """
    content = request.get_json()
    guest_controller.patch(guest_id, content)
    return make_response("Guest updated", HTTPStatus.OK)


@guest_bp.delete('/<int:guest_id>')
def delete_guest(guest_id: int) -> Response:
    """
    Delete a guest by ID
    ---
    tags:
      - Guest
    parameters:
      - in: path
        name: guest_id
        required: true
        schema:
          type: integer
        description: The ID of the guest
    responses:
      200:
        description: Guest deleted
    """

    guest_controller.delete(guest_id)
    return make_response("Guest deleted", HTTPStatus.OK)


@guest_bp.delete('')
def delete_guest_all() -> Response:
    """
    Delete all guests
    ---
    tags:
      - Guest
    responses:
      200:
        description: All guests deleted
    """
    guest_controller.delete_all()
    return make_response("All guests deleted", HTTPStatus.OK)

@guest_bp.get('/get-guest-after-address-id/<int:address_id>')
def get_guest_after_address_id(address_id: int) -> Response:
    """
    Get guests by address ID
    ---
    tags:
      - Guest
    parameters:
      - in: path
        name: address_id
        required: true
        schema:
          type: integer
        description: The ID of the address
    responses:
      200:
        description: Returns guests with the given address ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(guest_controller.get_guest_after_address_id(address_id)),
                         HTTPStatus.OK)