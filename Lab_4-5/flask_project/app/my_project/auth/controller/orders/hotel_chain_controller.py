from typing import List
from flask_project.app.my_project.auth.service import hotel_chain_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class HotelChainController(GeneralController):
    _service = hotel_chain_service

    def get_hotel_chain_after_city_id(self, city_id: int) -> List[object]:
        return self._service.get_hotel_chain_after_city_id(city_id)
