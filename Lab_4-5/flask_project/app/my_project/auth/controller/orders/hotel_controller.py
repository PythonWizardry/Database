from typing import List
from flask_project.app.my_project.auth.service import hotel_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class HotelController(GeneralController):
    _service = hotel_service

    def get_hotel_after_hotel_chain_id(self, hotel_chain_id: int) -> List[object]:
        return self._service.get_hotel_after_hotel_chain_id(hotel_chain_id)

    def get_hotel_after_city_id(self, city_id: int) -> List[object]:
        return self._service.get_hotel_after_city_id(city_id)