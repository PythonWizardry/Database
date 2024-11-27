from typing import List
from flask_project.app.my_project.auth.service import invoice_guest_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class InvoiceGuestController(GeneralController):
    _service = invoice_guest_service

    def get_reservation_after_guest(self, guest_id: int) -> List[object]:
        return self._service.get_reservation_after_guest(guest_id)

    def get_guest_after_reservation(self, reservation_id: int) -> List[object]:
        return self._service.get_guest_after_reservation(reservation_id)