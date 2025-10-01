from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import hotel_controller
from flask_project.app.my_project.auth.domain import Hotel

hotel_bp = Blueprint('hotel', __name__, url_prefix='/hotel')


@hotel_bp.get('')
def get_all_hotel() -> Response:
    """
    Get all hotels
    ---
    responses:
      200:
        description: Returns a list of hotels
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hotel_controller.find_all()), HTTPStatus.OK)


@hotel_bp.post('')
def create_hotel() -> Response:
    """
    Create a new hotel
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
              description: The name of the hotel
            description:
              type: string
              description: Description of the hotel
            is_active:
              type: boolean
              description: Is the hotel active
            city_id:
              type: integer
              description: City ID
            hotel_chain_id:
              type: integer
              description: Hotel chain ID
          required:
            - name
            - description
            - is_active
            - city_id
            - hotel_chain_id
    responses:
      201:
        description: Returns the created hotel
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.create(hotel)
    return make_response(jsonify(hotel.put_into_dto()), HTTPStatus.CREATED)


@hotel_bp.get('/<int:hotel_id>')
def get_hotel(hotel_id: int) -> Response:
    """
    Get a hotel by ID
    ---
    parameters:
      - in: path
        name: hotel_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel
    responses:
      200:
        description: Returns the hotel
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(hotel_controller.find_by_id(hotel_id)), HTTPStatus.OK)


@hotel_bp.put('/<int:hotel_id>')
def update_hotel(hotel_id: int) -> Response:
    """
    Update a hotel by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: hotel_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel
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
            is_active:
              type: boolean
            city_id:
              type: integer
            hotel_chain_id:
              type: integer
          required:
            - name
            - description
            - is_active
            - city_id
            - hotel_chain_id
    responses:
      200:
        description: Hotel updated
    """
    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.update(hotel_id, hotel)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.patch('/<int:hotel_id>')
def patch_hotel(hotel_id: int) -> Response:
    """
    Patch a hotel by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: hotel_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Hotel updated
    """
    content = request.get_json()
    hotel_controller.patch(hotel_id, content)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.delete('/<int:hotel_id>')
def delete_hotel(hotel_id: int) -> Response:
    """
    Delete a hotel by ID
    ---
    parameters:
      - in: path
        name: hotel_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel
    responses:
      200:
        description: Hotel deleted
    """
    hotel_controller.delete(hotel_id)
    return make_response("Hotel deleted", HTTPStatus.OK)


@hotel_bp.delete('')
def delete_hotel_all() -> Response:
    """
    Delete all hotels
    ---
    responses:
      200:
        description: All hotels deleted
    """
    hotel_controller.delete_all()
    return make_response("All hotels deleted", HTTPStatus.OK)

@hotel_bp.get('/get-hotel-after-hotel-chain-id/<int:hotel_chain_id>')
def get_hotel_after_hotel_chain_id(hotel_chain_id: int) -> Response:
    """
    Get hotels by hotel chain ID
    ---
    parameters:
      - in: path
        name: hotel_chain_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel chain
    responses:
      200:
        description: Returns hotels with the given hotel chain ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hotel_controller.get_hotel_after_hotel_chain_id(hotel_chain_id)),
                         HTTPStatus.OK)

@hotel_bp.get('/get-hotel-after-city-id/<int:city_id>')
def get_hotel_after_city_id(city_id: int) -> Response:
    """
    Get hotels by city ID
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
        description: Returns hotels with the given city ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hotel_controller.get_hotel_after_city_id(city_id)),
                         HTTPStatus.OK)