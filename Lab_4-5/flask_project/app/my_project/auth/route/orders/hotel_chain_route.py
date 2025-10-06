from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import hotel_chain_controller
from flask_project.app.my_project.auth.domain import HotelChain

hotel_chain_bp = Blueprint('hotel_chain', __name__, url_prefix='/hotel_chain')


@hotel_chain_bp.get('')
def get_all_hotel_chains() -> Response:
    """
    Get all hotel chains
    ---
    tags:
      - HotelChain
    responses:
      200:
        description: Returns a list of hotel chains
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hotel_chain_controller.find_all()), HTTPStatus.OK)


@hotel_chain_bp.post('')
def create_hotel_chain() -> Response:
    """
    Create a new hotel chain
    ---
    tags:
      - HotelChain
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
              description: The name of the hotel chain
            vat_id:
              type: string
              description: VAT ID
            email:
              type: string
              description: Contact email
            main_address:
              type: string
              description: Main address
            details:
              type: string
              description: Additional details
            is_active:
              type: boolean
              description: Is active
            city_id:
              type: integer
              description: City ID
          required:
            - name
            - vat_id
            - email
            - main_address
            - is_active
            - city_id
    responses:
      201:
        description: Returns the created hotel chain
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    hotel_chain = HotelChain.create_from_dto(content)
    hotel_chain_controller.create(hotel_chain)
    return make_response(jsonify(hotel_chain.put_into_dto()), HTTPStatus.CREATED)


@hotel_chain_bp.get('/<int:hotel_chain_id>')
def get_hotel_chain(hotel_chain_id: int) -> Response:
    """
    Get a hotel chain by ID
    ---
    tags:
      - HotelChain
    parameters:
      - in: path
        name: hotel_chain_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel chain
    responses:
      200:
        description: Returns the hotel chain
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(hotel_chain_controller.find_by_id(hotel_chain_id)), HTTPStatus.OK)


@hotel_chain_bp.put('/<int:hotel_chain_id>')
def update_hotel_chain(hotel_chain_id: int) -> Response:
    """
    Update a hotel chain by ID
    ---
    tags:
      - HotelChain
    consumes:
      - application/json
    parameters:
      - in: path
        name: hotel_chain_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel chain
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            vat_id:
              type: string
            email:
              type: string
            main_address:
              type: string
            details:
              type: string
            is_active:
              type: boolean
            city_id:
              type: integer
          required:
            - name
            - vat_id
            - email
            - main_address
            - is_active
            - city_id
    responses:
      200:
        description: Hotel chain updated
    """
    content = request.get_json()
    hotel_chain = HotelChain.create_from_dto(content)
    hotel_chain_controller.update(hotel_chain_id, hotel_chain)
    return make_response("Hotel chain updated", HTTPStatus.OK)


@hotel_chain_bp.patch('/<int:hotel_chain_id>')
def patch_hotel_chain(hotel_chain_id: int) -> Response:
    """
    Patch a hotel chain by ID
    ---
    tags:
      - HotelChain
    consumes:
      - application/json
    parameters:
      - in: path
        name: hotel_chain_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel chain
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Hotel chain updated
    """
    content = request.get_json()
    hotel_chain_controller.patch(hotel_chain_id, content)
    return make_response("Hotel chain updated", HTTPStatus.OK)


@hotel_chain_bp.delete('/<int:hotel_chain_id>')
def delete_hotel_chain(hotel_chain_id: int) -> Response:
    """
    Delete a hotel chain by ID
    ---
    tags:
      - HotelChain
    parameters:
      - in: path
        name: hotel_chain_id
        required: true
        schema:
          type: integer
        description: The ID of the hotel chain
    responses:
      200:
        description: Hotel chain deleted
    """
    hotel_chain_controller.delete(hotel_chain_id)
    return make_response("Hotel chain deleted", HTTPStatus.OK)


@hotel_chain_bp.delete('')
def delete_all_hotel_chains() -> Response:
    """
    Delete all hotel chains
    ---
    tags:
      - HotelChain
    responses:
      200:
        description: All hotel chains deleted
    """
    hotel_chain_controller.delete_all()
    return make_response("All hotel chains deleted", HTTPStatus.OK)

@hotel_chain_bp.get('/get-hotel-chain-after-city-id/<int:city_id>')
def get_hotel_chain_after_city_id(city_id: int) -> Response:
    """
    Get hotel chains by city ID
    ---
    tags:
      - HotelChain
    parameters:
      - in: path
        name: city_id
        required: true
        schema:
          type: integer
        description: The ID of the city
    responses:
      200:
        description: Returns hotel chains with the given city ID
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hotel_chain_controller.get_hotel_chain_after_city_id(city_id)),
                         HTTPStatus.OK)
