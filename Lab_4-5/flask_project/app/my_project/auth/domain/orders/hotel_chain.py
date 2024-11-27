from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class HotelChain(db.Model, IDto):
    __tablename__ = "hotel_chain"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(125), nullable=False)
    vat_id = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(125), nullable=False)
    main_address = db.Column(db.String(125), nullable=False)
    details = db.Column(db.TEXT(500))
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    city = db.relationship("City", backref="hotel_chain")

    def __repr__(self) -> str:
        return (f"HotelChain({self.id}, '{self.name}', '{self.vat_id}', {self.email}, "
                f"{self.main_address},  {self.details},  {self.is_active},  {self.city_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "vat_id": self.vat_id,
            "email": self.email,
            "main_address" : self.main_address,
            "details": self.details,
            "is_active": self.is_active,
            "city_id": self.city_id,
            "city_name": self.city.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HotelChain:
        obj = HotelChain(**dto_dict)
        return obj
