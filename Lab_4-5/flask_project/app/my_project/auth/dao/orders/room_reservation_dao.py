from typing import List, Dict, Any

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import RoomReservation
import sqlalchemy

class RoomReservationDAO(GeneralDAO):

    _domain_type = RoomReservation

    def get_room_after_reservation(self, reservation_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_room_after_reservation(:p1)"),
                                       {"p1": reservation_id}).mappings().all()
        return [dict(row) for row in result]

    def get_reservation_after_room(self, room_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_reservation_after_room(:p1)"),
                                       {"p1": room_id}).mappings().all()
        return [dict(row) for row in result]

    def insert_into_room_reservation(self, room_name: str, reservation_created: str, discount_percent: int, total_price: int):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_into_room_reservation(:room_name, :reservation_created, :discount_percent, :total_price)"),
            {"room_name": room_name, "reservation_created": reservation_created, "discount_percent": discount_percent, "total_price": total_price}
        )
        self._session.commit()
        return result

