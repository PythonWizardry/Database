from typing import List
from flask_project.app.my_project.auth.dao import status_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class StatusService(GeneralService):

    _dao = status_dao