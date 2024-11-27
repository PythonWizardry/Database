from typing import List
from flask_project.app.my_project.auth.service import review_service
from flask_project.app.my_project.auth.controller.general_controller import GeneralController


class ReviewController(GeneralController):
    _service = review_service

    def insert_into_review(self, guest_id: int, review_context: str):
        return self._service.insert_into_review(guest_id, review_context)