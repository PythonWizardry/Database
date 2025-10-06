from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import status_controller
from flask_project.app.my_project.auth.domain import Status

status_bp = Blueprint('status', __name__, url_prefix='/status')


@status_bp.get('')
def get_all_status() -> Response:
    """
    Get all statuses
    ---
    tags:
      - Status
    responses:
      200:
        description: Returns a list of statuses
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(status_controller.find_all()), HTTPStatus.OK)


@status_bp.post('')
def create_status() -> Response:
    """
    Create a new status
    ---
    tags:
      - Status
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            status_name:
              type: string
              description: The name of the status
          required:
            - status_name
    responses:
      201:
        description: Returns the created status
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    status = Status.create_from_dto(content)
    status_controller.create(status)
    return make_response(jsonify(status.put_into_dto()), HTTPStatus.CREATED)


@status_bp.get('/<int:status_id>')
def get_status(status_id: int) -> Response:
    """
    Get a status by ID
    ---
    tags:
      - Status
    parameters:
      - in: path
        name: status_id
        required: true
        schema:
          type: integer
        description: The ID of the status
    responses:
      200:
        description: Returns the status
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(status_controller.find_by_id(status_id)), HTTPStatus.OK)


@status_bp.put('/<int:status_id>')
def update_status(status_id: int) -> Response:
    """
    Update a status by ID
    ---
    tags:
      - Status
    consumes:
      - application/json
    parameters:
      - in: path
        name: status_id
        required: true
        schema:
          type: integer
        description: The ID of the status
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            status_name:
              type: string
          required:
            - status_name
    responses:
      200:
        description: Status updated
    """
    content = request.get_json()
    status = Status.create_from_dto(content)
    status_controller.update(status_id, status)
    return make_response("Status updated", HTTPStatus.OK)


@status_bp.patch('/<int:status_id>')
def patch_status(status_id: int) -> Response:
    """
    Patch a status by ID
    ---
    tags:
      - Status
    consumes:
      - application/json
    parameters:
      - in: path
        name: status_id
        required: true
        schema:
          type: integer
        description: The ID of the status
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Status updated
    """
    content = request.get_json()
    status_controller.patch(status_id, content)
    return make_response("Status updated", HTTPStatus.OK)


@status_bp.delete('/<int:status_id>')
def delete_status(status_id: int) -> Response:
    """
    Delete a status by ID
    ---
    tags:
      - Status
    parameters:
      - in: path
        name: status_id
        required: true
        schema:
          type: integer
        description: The ID of the status
    responses:
      200:
        description: Status deleted
    """
    status_controller.delete(status_id)
    return make_response("Status deleted", HTTPStatus.OK)
