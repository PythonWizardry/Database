from typing import List
from flask_project.app.my_project.auth.service import guest_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class GuestController(GeneralController):
    _service = guest_service

    def get_guest_after_address_id(self, address_id: int) -> List[object]:
        return self._service.get_guest_after_address_id(address_id)