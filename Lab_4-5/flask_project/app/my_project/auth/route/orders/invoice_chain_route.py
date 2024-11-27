from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flask_project.app.my_project.auth.controller import invoice_chain_controller
from flask_project.app.my_project.auth.domain import InvoiceChain

invoice_chain_bp = Blueprint('invoice_chain', __name__, url_prefix='/invoice_chain')


@invoice_chain_bp.get('')
def get_all_invoice_chain() -> Response:

    return make_response(jsonify(invoice_chain_controller.find_all()), HTTPStatus.OK)


@invoice_chain_bp.post('')
def create_invoice_chain() -> Response:

    content = request.get_json()
    invoice_chain = InvoiceChain.create_from_dto(content)
    invoice_chain_controller.create(invoice_chain)
    return make_response(jsonify(invoice_chain.put_into_dto()), HTTPStatus.CREATED)


@invoice_chain_bp.get('/<int:invoice_chain_id>')
def get_invoice_chain(invoice_chain_id: int) -> Response:

    return make_response(jsonify(invoice_chain_controller.find_by_id(invoice_chain_id)), HTTPStatus.OK)


@invoice_chain_bp.put('/<int:invoice_chain_id>')
def update_invoice_chain(invoice_chain_id: int) -> Response:

    content = request.get_json()
    invoice_chain = InvoiceChain.create_from_dto(content)
    invoice_chain_controller.update(invoice_chain_id, invoice_chain)
    return make_response("InvoiceChain updated", HTTPStatus.OK)


@invoice_chain_bp.patch('/<int:invoice_chain_id>')
def patch_invoice_chain(invoice_chain_id: int) -> Response:

    content = request.get_json()
    invoice_chain_controller.patch(invoice_chain_id, content)
    return make_response("InvoiceChain updated", HTTPStatus.OK)


@invoice_chain_bp.delete('/<int:invoice_chain_id>')
def delete_invoice_chain(invoice_chain_id: int) -> Response:

    invoice_chain_controller.delete(invoice_chain_id)
    return make_response("InvoiceChain deleted", HTTPStatus.OK)


@invoice_chain_bp.delete('')
def delete_invoice_chain_all() -> Response:
    invoice_chain_controller.delete_all()
    return make_response("All invoice_chains deleted", HTTPStatus.OK)

@invoice_chain_bp.get('/get-invoice-chain-after-hotel-chain-id/<int:hotel_chain_id>')
def get_invoice_chain_after_hotel_chain_id(hotel_chain_id: int) -> Response:
    return make_response(jsonify(invoice_chain_controller.get_invoice_chain_after_hotel_chain_id(hotel_chain_id)),
                         HTTPStatus.OK)

@invoice_chain_bp.get('/calculate-invoice-chain/<string:type>')
def procedure_calculate_invoice_chain(type: str) -> Response:
    return make_response(jsonify(invoice_chain_controller.procedure_calculate_invoice_chain(type)), HTTPStatus.OK)
