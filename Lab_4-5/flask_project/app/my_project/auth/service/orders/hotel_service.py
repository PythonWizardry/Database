from typing import List
from flask_project.app.my_project.auth.dao import hotel_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class HotelService(GeneralService):

    _dao = hotel_dao

    def get_hotel_after_hotel_chain_id(self, hotel_chain_id: int) -> List[object]:
        return self._dao.get_hotel_after_hotel_chain_id(hotel_chain_id)

    def get_hotel_after_city_id(self, city_id: int) -> List[object]:
        return self._dao.get_hotel_after_city_id(city_id)