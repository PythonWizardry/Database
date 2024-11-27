from typing import List
from flask_project.app.my_project.auth.dao import invoice_chain_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class InvoiceChainService(GeneralService):

    _dao = invoice_chain_dao

    def get_invoice_chain_after_hotel_chain_id(self, hotel_chain_id: int) -> List[object]:
        return self._dao.get_invoice_chain_after_hotel_chain_id(hotel_chain_id)

    def procedure_calculate_invoice_chain(self, type: str):
        return self._dao.procedure_calculate_invoice_chain(type)