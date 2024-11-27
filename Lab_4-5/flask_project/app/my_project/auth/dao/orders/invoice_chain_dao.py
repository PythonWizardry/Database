from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import InvoiceChain
import sqlalchemy

class InvoiceChainDAO(GeneralDAO):

    _domain_type = InvoiceChain

    def get_invoice_chain_after_hotel_chain_id(self, hotel_chain_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_invoice_chain_after_hotel_chain_id(:p1)"),
                                       {"p1": hotel_chain_id}).mappings().all()
        return [dict(row) for row in result]

    def procedure_calculate_invoice_chain(self, type: str) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL procedure_calculate_invoice_chain(:p1)"),
                                       {'p1': type}).mappings().all()
        return [dict(row) for row in result]

