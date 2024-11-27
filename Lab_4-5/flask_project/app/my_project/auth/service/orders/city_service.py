from typing import List
from flask_project.app.my_project.auth.dao import city_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class CityService(GeneralService):

    _dao = city_dao

    def package_insert(self):
        return self._dao.package_insert()