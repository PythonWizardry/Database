from typing import List
from flask_project.app.my_project.auth.service import status_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class StatusController(GeneralController):
    _service = status_service