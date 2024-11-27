from typing import List
from flask_project.app.my_project.auth.service import invoice_chain_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class InvoiceChainController(GeneralController):
    _service = invoice_chain_service

    def get_invoice_chain_after_hotel_chain_id(self, hotel_chain_id: int) -> List[object]:
        return self._service.get_invoice_chain_after_hotel_chain_id(hotel_chain_id)

    def procedure_calculate_invoice_chain(self, type: str):
        return self._service.procedure_calculate_invoice_chain(type)