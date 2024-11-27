from typing import List
from flask_project.app.my_project.auth.service import room_reservation_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class RoomReservationController(GeneralController):
    _service = room_reservation_service

    def get_room_after_reservation(self, reservation_id: int) -> List[object]:
        return self._service.get_room_after_reservation(reservation_id)

    def get_reservation_after_room(self, room_id: int) -> List[object]:
        return self._service.get_reservation_after_room(room_id)

    def insert_into_room_reservation(self, room_name: str, reservation_created: str, discount_percent: int,
                                     total_price: int):
        return self._service.insert_into_room_reservation(room_name, reservation_created, discount_percent, total_price)