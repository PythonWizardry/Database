from typing import List, Dict, Any
from flask_project.app.my_project.auth.dao.general_dao import GeneralDAO
from flask_project.app.my_project.auth.domain import Review
import sqlalchemy

class ReviewDAO(GeneralDAO):

    _domain_type = Review

    def insert_into_review(self, guest_id: int, review_context: str):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_into_review(:guest_id, :review_context)"),
            {"guest_id": guest_id, "review_context": review_context}
        )
        self._session.commit()
        return result
