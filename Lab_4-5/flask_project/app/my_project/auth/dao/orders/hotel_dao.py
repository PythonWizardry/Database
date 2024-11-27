from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Hotel
import sqlalchemy

class HotelDAO(GeneralDAO):

    _domain_type = Hotel

    def get_hotel_after_hotel_chain_id(self, hotel_chain_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_hotel_after_hotel_chain_id(:p1)"),
                                       {"p1": hotel_chain_id}).mappings().all()
        return [dict(row) for row in result]

    def get_hotel_after_city_id(self, city_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_hotel_after_city_id(:p1)"),
                                       {"p1": city_id}).mappings().all()
        return [dict(row) for row in result]

