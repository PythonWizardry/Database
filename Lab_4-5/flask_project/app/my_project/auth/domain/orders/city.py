from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class City(db.Model, IDto):
    __tablename__ = "city"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(125), nullable=False)

    def __repr__(self) -> str:
        return f"City({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        obj = City(**dto_dict)
        return obj
