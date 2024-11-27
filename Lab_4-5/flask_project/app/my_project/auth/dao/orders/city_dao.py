from typing import List

from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import City
import sqlalchemy

class CityDAO(GeneralDAO):

    _domain_type = City


    def package_insert(self):
        result = self._session.execute(
            sqlalchemy.text("CALL package_insert()"),
            {}
        )
        self._session.commit()
        return result

