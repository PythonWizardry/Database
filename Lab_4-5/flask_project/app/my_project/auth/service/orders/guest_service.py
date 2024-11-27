from typing import List
from flask_project.app.my_project.auth.dao import guest_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class GuestService(GeneralService):

    _dao = guest_dao

    def get_guest_after_address_id(self, address_id: int) -> List[object]:
        return self._dao.get_guest_after_address_id(address_id)