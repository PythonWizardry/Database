from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import hotel_controller
from flask_project.app.my_project.auth.domain import Hotel

hotel_bp = Blueprint('hotel', __name__, url_prefix='/hotel')


@hotel_bp.get('')
def get_all_hotel() -> Response:

    return make_response(jsonify(hotel_controller.find_all()), HTTPStatus.OK)


@hotel_bp.post('')
def create_hotel() -> Response:

    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.create(hotel)
    return make_response(jsonify(hotel.put_into_dto()), HTTPStatus.CREATED)


@hotel_bp.get('/<int:hotel_id>')
def get_hotel(hotel_id: int) -> Response:

    return make_response(jsonify(hotel_controller.find_by_id(hotel_id)), HTTPStatus.OK)


@hotel_bp.put('/<int:hotel_id>')
def update_hotel(hotel_id: int) -> Response:

    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.update(hotel_id, hotel)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.patch('/<int:hotel_id>')
def patch_hotel(hotel_id: int) -> Response:

    content = request.get_json()
    hotel_controller.patch(hotel_id, content)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.delete('/<int:hotel_id>')
def delete_hotel(hotel_id: int) -> Response:

    hotel_controller.delete(hotel_id)
    return make_response("Hotel deleted", HTTPStatus.OK)


@hotel_bp.delete('')
def delete_hotel_all() -> Response:
    hotel_controller.delete_all()
    return make_response("All hotels deleted", HTTPStatus.OK)

@hotel_bp.get('/get-hotel-after-hotel-chain-id/<int:hotel_chain_id>')
def get_hotel_after_hotel_chain_id(hotel_chain_id: int) -> Response:
    return make_response(jsonify(hotel_controller.get_hotel_after_hotel_chain_id(hotel_chain_id)),
                         HTTPStatus.OK)

@hotel_bp.get('/get-hotel-after-city-id/<int:city_id>')
def get_hotel_after_city_id(city_id: int) -> Response:
    return make_response(jsonify(hotel_controller.get_hotel_after_city_id(city_id)),
                         HTTPStatus.OK)