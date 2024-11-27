from typing import List

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Status
import sqlalchemy

class StatusDAO(GeneralDAO):

    _domain_type = Status

    def insert_into_room_reservation(self, room_name: str, reservation_created: str, discount_percent: int, total_price: int):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_into_room_reservation(:room_name, :reservation_created, :discount_percent, :total_price)"),
            {"room_name": room_name, "reservation_created": reservation_created, "discount_percent": discount_percent, "total_price": total_price}
        )
        self._session.commit()
        return result

