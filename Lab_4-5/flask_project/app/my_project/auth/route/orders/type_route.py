from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import type_controller
from flask_project.app.my_project.auth.domain import Type

type_bp = Blueprint('type', __name__, url_prefix='/type')


@type_bp.get('')
def get_all_type() -> Response:
    """
    Get all types
    ---
    responses:
      200:
        description: Returns a list of types
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(type_controller.find_all()), HTTPStatus.OK)


@type_bp.post('')
def create_type() -> Response:
    """
    Create a new type
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
            name:
              type: string
              description: The name of the type
          required:
            - name
    responses:
      201:
        description: Returns the created type
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    type_instance = Type.create_from_dto(content)
    type_controller.create(type_instance)
    return make_response(jsonify(type_instance.put_into_dto()), HTTPStatus.CREATED)


@type_bp.get('/<int:type_id>')
def get_type(type_id: int) -> Response:
    """
    Get a type by ID
    ---
    parameters:
      - in: path
        name: type_id
        required: true
        schema:
          type: integer
        description: The ID of the type
    responses:
      200:
        description: Returns the type
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(type_controller.find_by_id(type_id)), HTTPStatus.OK)


@type_bp.put('/<int:type_id>')
def update_type(type_id: int) -> Response:
    """
    Update a type by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: type_id
        required: true
        schema:
          type: integer
        description: The ID of the type
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
          required:
            - name
    responses:
      200:
        description: Type updated
    """
    content = request.get_json()
    type_instance = Type.create_from_dto(content)
    type_controller.update(type_id, type_instance)
    return make_response("Type updated", HTTPStatus.OK)


@type_bp.patch('/<int:type_id>')
def patch_type(type_id: int) -> Response:
    """
    Patch a type by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: type_id
        required: true
        schema:
          type: integer
        description: The ID of the type
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Type updated
    """
    content = request.get_json()
    type_controller.patch(type_id, content)
    return make_response("Type updated", HTTPStatus.OK)


@type_bp.delete('/<int:type_id>')
def delete_type(type_id: int) -> Response:
    """
    Delete a type by ID
    ---
    parameters:
      - in: path
        name: type_id
        required: true
        schema:
          type: integer
        description: The ID of the type
    responses:
      200:
        description: Type deleted
    """
    type_controller.delete(type_id)
    return make_response("Type deleted", HTTPStatus.OK)


@type_bp.delete('')
def delete_type_all() -> Response:
    """
    Delete all types
    ---
    responses:
      200:
        description: All types deleted
    """
    type_controller.delete_all()
    return make_response("All types deleted", HTTPStatus.OK)
