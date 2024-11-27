from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import HotelChain
import sqlalchemy

class HotelChainDAO(GeneralDAO):

    _domain_type = HotelChain

    def get_hotel_chain_after_city_id(self, city_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_hotel_chain_after_city_id(:p1)"),
                                       {"p1": city_id}).mappings().all()
        return [dict(row) for row in result]

