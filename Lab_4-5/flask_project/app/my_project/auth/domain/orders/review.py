from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Review(db.Model, IDto):
    __tablename__ = "review"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    guest_id = db.Column(db.Integer, nullable=False)
    review_context = db.Column(db.TEXT(250), nullable=False)

    def __repr__(self) -> str:
        return f"Review({self.id}, '{self.guest_id}', '{self.review_context}', {self.email}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "guest_id": self.guest_id,
            "review_context": self.review_context
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        obj = Review(**dto_dict)
        return obj
