from typing import List
from flask_project.app.my_project.auth.dao import room_reservation_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class RoomReservationService(GeneralService):

    _dao = room_reservation_dao

    def get_room_after_reservation(self, reservation_id: int) -> List[object]:
        return self._dao.get_room_after_reservation(reservation_id)

    def get_reservation_after_room(self, room_id: int) -> List[object]:
        return self._dao.get_reservation_after_room(room_id)

    def insert_into_room_reservation(self, room_name: str, reservation_created: str, discount_percent: int, total_price: int):
        return self._dao.insert_into_room_reservation(room_name, reservation_created, discount_percent, total_price)