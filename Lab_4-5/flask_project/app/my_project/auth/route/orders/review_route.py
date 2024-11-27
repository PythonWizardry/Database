from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import review_controller
from flask_project.app.my_project.auth.domain import Review

review_bp = Blueprint('review', __name__, url_prefix='/review')


@review_bp.get('')
def get_all_reviews() -> Response:

    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_review() -> Response:

    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:

    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:

    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:

    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:

    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)


@review_bp.delete('')
def delete_reviews_all() -> Response:
    review_controller.delete_all()
    return make_response("All reviews deleted", HTTPStatus.OK)

@review_bp.post('/insert-into-review')
def create_reviews() -> Response:
    content = request.get_json()
    guest_id = content['guest_id']
    review_context = content['review_context']
    review_controller.insert_into_review(guest_id, review_context)
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.CREATED)
