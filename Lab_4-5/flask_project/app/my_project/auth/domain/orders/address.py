from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Address(db.Model, IDto):
    __tablename__ = "address"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    street = db.Column(db.String(125), nullable=False)
    house_number = db.Column(db.String(25), nullable=False)
    apartment_number = db.Column(db.String(25))

    def __repr__(self) -> str:
        return f"Address({self.id}, '{self.street}', '{self.house_number}', {self.apartment_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "street": self.street,
            "house_number": self.house_number,
            "apartment_number": self.apartment_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Address:
        obj = Address(**dto_dict)
        return obj