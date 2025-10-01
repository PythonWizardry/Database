from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import address_controller
from flask_project.app.my_project.auth.domain import Address

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.get('')
def get_all_address() -> Response:
    """
    Get all addresses
    ---
    responses:
      200:
        description: Returns a list of addresses
    """
    return make_response(jsonify(address_controller.find_all()), HTTPStatus.OK)


@address_bp.post('')
def create_address() -> Response:
    """
    Create a new address
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
            street:
              type: string
              description: The street name
            house_number:
              type: string
              description: The house number
            apartment_number:
              type: string
              description: The apartment number
          required:
            - street
            - house_number
    responses:
      201:
        description: Returns the created address
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.get('/<int:address_id>')
def get_address(address_id: int) -> Response:
    """
    Get an address by ID
    ---
    parameters:
      - in: path
        name: address_id
        required: true
        schema:
          type: integer
        description: The ID of the address
    responses:
      200:
        description: Returns the address
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(address_controller.find_by_id(address_id)), HTTPStatus.OK)


@address_bp.put('/<int:address_id>')
def update_address(address_id: int) -> Response:
    """
    Update an address by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: address_id
        required: true
        schema:
          type: integer
        description: The ID of the address
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            street:
              type: string
            house_number:
              type: string
            apartment_number:
              type: string
          required:
            - street
            - house_number
    responses:
      200:
        description: Address updated
    """
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update(address_id, address)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.patch('/<int:address_id>')
def patch_address(address_id: int) -> Response:
    """
    Patch an address by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: address_id
        required: true
        schema:
          type: integer
        description: The ID of the address
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Address updated
    """
    content = request.get_json()
    address_controller.patch(address_id, content)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.delete('/<int:address_id>')
def delete_address(address_id: int) -> Response:
    """
    Delete an address by ID
    ---
    parameters:
      - in: path
        name: address_id
        required: true
        schema:
          type: integer
        description: The ID of the address
    responses:
      200:
        description: Address deleted
    """
    address_controller.delete(address_id)
    return make_response("Address deleted", HTTPStatus.OK)



