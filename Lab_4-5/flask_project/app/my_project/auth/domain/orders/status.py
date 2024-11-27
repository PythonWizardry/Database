from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Status(db.Model, IDto):
    __tablename__ = "status"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(45), nullable=False)


    def __repr__(self) -> str:
        return f"Status({self.id}, '{self.status_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "status_name": self.status_name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Status:
        obj = Status(**dto_dict)
        return obj
