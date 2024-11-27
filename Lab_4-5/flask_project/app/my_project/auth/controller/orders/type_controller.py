from typing import List
from flask_project.app.my_project.auth.service import type_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class TypeController(GeneralController):
    _service = type_service