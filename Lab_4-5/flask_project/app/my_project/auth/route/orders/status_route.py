from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import status_controller
from flask_project.app.my_project.auth.domain import Status

status_bp = Blueprint('status', __name__, url_prefix='/status')


@status_bp.get('')
def get_all_status() -> Response:
    return make_response(jsonify(status_controller.find_all()), HTTPStatus.OK)


@status_bp.post('')
def create_status() -> Response:
    content = request.get_json()
    status = Status.create_from_dto(content)
    status_controller.create(status)
    return make_response(jsonify(status.put_into_dto()), HTTPStatus.CREATED)


@status_bp.get('/<int:status_id>')
def get_status(status_id: int) -> Response:
    return make_response(jsonify(status_controller.find_by_id(status_id)), HTTPStatus.OK)


@status_bp.put('/<int:status_id>')
def update_status(status_id: int) -> Response:
    content = request.get_json()
    status = Status.create_from_dto(content)
    status_controller.update(status_id, status)
    return make_response("Status updated", HTTPStatus.OK)


@status_bp.patch('/<int:status_id>')
def patch_status(status_id: int) -> Response:
    content = request.get_json()
    status_controller.patch(status_id, content)
    return make_response("Status updated", HTTPStatus.OK)


@status_bp.delete('/<int:status_id>')
def delete_status(status_id: int) -> Response:
    status_controller.delete(status_id)
    return make_response("Status deleted", HTTPStatus.OK)
