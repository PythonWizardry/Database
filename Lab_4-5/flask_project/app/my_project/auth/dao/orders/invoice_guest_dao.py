from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import InvoiceGuest
import sqlalchemy

class InvoiceGuestDAO(GeneralDAO):

    _domain_type = InvoiceGuest

    def get_reservation_after_guest(self, guest_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_reservation_after_guest(:p1)"),
                                       {"p1": guest_id}).mappings().all()
        return [dict(row) for row in result]

    def get_guest_after_reservation(self, reservation_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_guest_after_reservation(:p1)"),
                                       {"p1": reservation_id}).mappings().all()
        return [dict(row) for row in result]



