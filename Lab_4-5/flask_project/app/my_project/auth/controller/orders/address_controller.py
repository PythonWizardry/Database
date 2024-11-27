from flask_project.app.my_project.auth.service import address_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class AddressController(GeneralController):
    _service = address_service