from typing import List
from flask_project.app.my_project.auth.service import city_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class CityController(GeneralController):
    _service = city_service

    def package_insert(self):
        return self._service.package_insert()