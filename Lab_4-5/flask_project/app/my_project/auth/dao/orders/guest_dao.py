from typing import List, Dict, Any
from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Guest
import sqlalchemy

class GuestDAO(GeneralDAO):

    _domain_type = Guest

    def get_guest_after_address_id(self, address_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_guest_after_address_id(:p1)"),
                                       {"p1": address_id}).mappings().all()
        return [dict(row) for row in result]
