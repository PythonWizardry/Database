from typing import List
from flask_project.app.my_project.auth.dao import invoice_guest_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class InvoiceGuestService(GeneralService):

    _dao = invoice_guest_dao

    def get_reservation_after_guest(self, guest_id: int) -> List[object]:
        return self._dao.get_reservation_after_guest(guest_id)

    def get_guest_after_reservation(self, reservation_id: int) -> List[object]:
        return self._dao.get_guest_after_reservation(reservation_id)