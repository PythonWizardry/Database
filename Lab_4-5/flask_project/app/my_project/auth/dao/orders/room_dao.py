from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Room
import sqlalchemy

class RoomDAO(GeneralDAO):

    _domain_type = Room

    def get_room_after_status_id(self, status_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_room_after_status_id(:p1)"),
                                       {"p1": status_id}).mappings().all()
        return [dict(row) for row in result]

    def get_room_after_hotel_id(self, hotel_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_room_after_hotel_id(:p1)"),
                                       {"p1": hotel_id}).mappings().all()
        return [dict(row) for row in result]

    def get_room_after_type_id(self, type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_room_after_type_id(:p1)"),
                                       {"p1": type_id}).mappings().all()
        return [dict(row) for row in result]

