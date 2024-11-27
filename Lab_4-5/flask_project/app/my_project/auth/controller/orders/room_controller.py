from typing import List
from flask_project.app.my_project.auth.service import room_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class RoomController(GeneralController):
    _service = room_service

    def get_room_after_status_id(self, status_id: int) -> List[object]:
        return self._service.get_room_after_status_id(status_id)

    def get_room_after_hotel_id(self, hotel_id: int) -> List[object]:
        return self._service.get_room_after_hotel_id(hotel_id)

    def get_room_after_type_id(self, type_id: int) -> List[object]:
        return self._service.get_room_after_type_id(type_id)