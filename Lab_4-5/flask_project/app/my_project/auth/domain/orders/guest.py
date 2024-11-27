from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Guest(db.Model, IDto):
    __tablename__ = "guest"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(125), nullable=False)
    surname = db.Column(db.String(125), nullable=False)
    email = db.Column(db.String(125), nullable=False)
    phone = db.Column(db.String(125))
    details = db.Column(db.TEXT(500))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    address = db.relationship("Address", backref="guest")

    def __repr__(self) -> str:
        return (f"Guest({self.id}, '{self.name}', '{self.surname}', {self.email}, "
                f"{self.phone},  {self.details},  {self.address_id},  {self.address.street})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "phone" : self.phone,
            "details": self.details,
            "address_id": self.address_id,
            "address_street": self.address.street
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Guest:
        obj = Guest(**dto_dict)
        return obj
