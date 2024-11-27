from typing import List
from flask_project.app.my_project.auth.service import reservation_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class ReservationController(GeneralController):
    _service = reservation_service

    def get_reservation_after_guest_id(self, guest_id: int) -> List[object]:
        return self._service.get_reservation_after_guest_id(guest_id)

    def get_reservation_after_status_id(self, status_id: int) -> List[object]:
        return self._service.get_reservation_after_status_id(status_id)