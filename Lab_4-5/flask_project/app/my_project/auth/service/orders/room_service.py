from typing import List
from flask_project.app.my_project.auth.dao import room_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class RoomService(GeneralService):

    _dao = room_dao

    def get_room_after_status_id(self, status_id: int) -> List[object]:
        return self._dao.get_room_after_status_id(status_id)

    def get_room_after_hotel_id(self, hotel_id: int) -> List[object]:
        return self._dao.get_room_after_hotel_id(hotel_id)

    def get_room_after_type_id(self, type_id: int) -> List[object]:
        return self._dao.get_room_after_type_id(type_id)