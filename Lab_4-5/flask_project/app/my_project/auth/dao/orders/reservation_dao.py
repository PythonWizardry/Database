from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Reservation
import sqlalchemy

class ReservationDAO(GeneralDAO):

    _domain_type = Reservation

    def get_reservation_after_guest_id(self, guest_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_reservation_after_guest_id(:p1)"),
                                       {"p1": guest_id}).mappings().all()
        return [dict(row) for row in result]

    def get_reservation_after_status_id(self, status_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_reservation_after_status_id(:p1)"),
                                       {"p1": status_id}).mappings().all()
        return [dict(row) for row in result]

