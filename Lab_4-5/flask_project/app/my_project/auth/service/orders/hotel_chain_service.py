from typing import List
from flask_project.app.my_project.auth.dao import hotel_chain_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class HotelChainService(GeneralService):

    _dao = hotel_chain_dao

    def get_hotel_chain_after_city_id(self, city_id: int) -> List[object]:
        return self._dao.get_hotel_chain_after_city_id(city_id)