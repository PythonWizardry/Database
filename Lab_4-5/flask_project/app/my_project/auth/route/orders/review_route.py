from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import review_controller
from flask_project.app.my_project.auth.domain import Review

review_bp = Blueprint('review', __name__, url_prefix='/review')


@review_bp.get('')
def get_all_reviews() -> Response:
    """
    Get all reviews
    ---
    responses:
      200:
        description: Returns a list of reviews
    """
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.post('')
def create_review() -> Response:

    """
    Create a new review
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
              description: The ID of the guest
            review_context:
              type: string
              description: The content of the review
          required:
            - guest_id
            - review_context
    responses:
      201:
        description: Returns the created review
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:

    """
    Get a review by ID
    ---
    parameters:
      - in: path
        name: review_id
        required: true
        schema:
          type: integer
        description: The ID of the review
    responses:
      200:
        description: Returns the review
    """

    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:

    """
    Update a review by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: review_id
        required: true
        schema:
          type: integer
        description: The ID of the review
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            guest_id:
              type: integer
            review_context:
              type: string
          required:
            - guest_id
            - review_context
    responses:
      200:
        description: Review updated
    """

    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:

    """
    Patch a review by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: review_id
        required: true
        schema:
          type: integer
        description: The ID of the review
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Review updated
    """

    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    """
    Delete a review by ID
    ---
    parameters:
      - in: path
        name: review_id
        required: true
        schema:
          type: integer
        description: The ID of the review
    responses:
      200:
        description: Review deleted
    """
    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)


@review_bp.delete('')
def delete_reviews_all() -> Response:
    """
    Delete all reviews
    ---
    responses:
      200:
        description: All reviews deleted
    """
    review_controller.delete_all()
    return make_response("All reviews deleted", HTTPStatus.OK)

@review_bp.post('/insert-into-review')
def create_reviews() -> Response:
    content = request.get_json()
    guest_id = content['guest_id']
    review_context = content['review_context']
    review_controller.insert_into_review(guest_id, review_context)
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.CREATED)
