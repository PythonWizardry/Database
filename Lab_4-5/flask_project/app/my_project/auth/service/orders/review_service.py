from typing import List
from flask_project.app.my_project.auth.dao import review_dao
from flask_project.app.my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):

    _dao = review_dao

    def insert_into_review(self, guest_id: int, review_context: str):
        return self._dao.insert_into_review(guest_id, review_context)