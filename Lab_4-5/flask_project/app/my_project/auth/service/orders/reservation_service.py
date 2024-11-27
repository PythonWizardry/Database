from typing import List
from flask_project.app.my_project.auth.dao import reservation_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class ReservationService(GeneralService):

    _dao = reservation_dao

    def get_reservation_after_guest_id(self, guest_id: int) -> List[object]:
        return self._dao.get_reservation_after_guest_id(guest_id)

    def get_reservation_after_status_id(self, status_id: int) -> List[object]:
        return self._dao.get_reservation_after_status_id(status_id)