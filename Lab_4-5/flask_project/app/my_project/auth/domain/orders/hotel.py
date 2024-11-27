from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Hotel(db.Model, IDto):
    __tablename__ = "hotel"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(125), nullable=False)
    description = db.Column(db.TEXT(500))
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship("City", backref="hotel")
    hotel_chain_id = db.Column(db.Integer, db.ForeignKey('hotel_chain.id'), nullable=False)
    hotel_chain = db.relationship("HotelChain", backref="hotel")

    def __repr__(self) -> str:
        return (f"Hotel({self.id}, '{self.name}', '{self.description}', {self.is_active}, "
                f"{self.city_id},  {self.hotel_chain_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active,
            "city_id" : self.city_id,
            "hotel_chain_id": self.hotel_chain_id,
            "city_name": self.city.name,
            "hotel_chain_name": self.hotel_chain.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Hotel:
        obj = Hotel(**dto_dict)
        return obj
