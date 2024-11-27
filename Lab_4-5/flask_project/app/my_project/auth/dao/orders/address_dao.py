from typing import List

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Address
import sqlalchemy

class AddressDAO(GeneralDAO):

    _domain_type = Address

