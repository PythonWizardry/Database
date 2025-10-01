from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import city_controller
from flask_project.app.my_project.auth.domain import City

city_bp = Blueprint('city', __name__, url_prefix='/city')


@city_bp.get('')
def get_all_cities() -> Response:
    """
    Get all cities
    ---
    responses:
      200:
        description: Returns a list of cities
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.OK)


@city_bp.post('')
def create_city() -> Response:
    """
    Create a new city
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
              description: The name of the city
          required:
            - name
    responses:
      201:
        description: Returns the created city
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.create(city)
    return make_response(jsonify(city.put_into_dto()), HTTPStatus.CREATED)


@city_bp.get('/<int:city_id>')
def get_city(city_id: int) -> Response:
    """
    Get a city by ID
    ---
    parameters:
      - in: path
        name: city_id
        required: true
        schema:
          type: integer
        description: The ID of the city
    responses:
      200:
        description: Returns the city
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(city_controller.find_by_id(city_id)), HTTPStatus.OK)


@city_bp.put('/<int:city_id>')
def update_city(city_id: int) -> Response:
    """
    Update a city by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: city_id
        required: true
        schema:
          type: integer
        description: The ID of the city
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
        description: City updated
    """
    content = request.get_json()
    city = City.create_from_dto(content)
    city_controller.update(city_id, city)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.patch('/<int:city_id>')
def patch_city(city_id: int) -> Response:
    """
    Patch a city by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: city_id
        required: true
        schema:
          type: integer
        description: The ID of the city
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: City updated
    """
    content = request.get_json()
    city_controller.patch(city_id, content)
    return make_response("City updated", HTTPStatus.OK)


@city_bp.delete('/<int:city_id>')
def delete_city(city_id: int) -> Response:
    """
    Delete a city by ID
    ---
    parameters:
      - in: path
        name: city_id
        required: true
        schema:
          type: integer
        description: The ID of the city
    responses:
      200:
        description: City deleted
    """
    city_controller.delete(city_id)
    return make_response("City deleted", HTTPStatus.OK)


@city_bp.delete('')
def delete_all_cities() -> Response:
    """
    Delete all cities
    ---
    responses:
      200:
        description: All cities deleted
    """
    city_controller.delete_all()
    return make_response("All cities deleted", HTTPStatus.OK)

@city_bp.post('/package-insert')
def create_packages() -> Response:
    city_controller.package_insert()
    return make_response(jsonify(city_controller.find_all()), HTTPStatus.CREATED)
