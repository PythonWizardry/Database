from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Room(db.Model, IDto):
    __tablename__ = "room"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.TEXT(500))
    price = db.Column(db.DECIMAL(10,2), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    hotel = db.relationship("Hotel", backref="room")
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    status = db.relationship("Status", backref="room")
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    type = db.relationship("Type", backref="room")

    def __repr__(self) -> str:
        return (f"Room({self.id}, '{self.name}', '{self.description}', {self.price}, "
                f"{self.hotel_id},  {self.status_id},  {self.type_id},  {self.hotel.name}, {self.status.name}, "
                f"{self.type.name})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "hotel_id" : self.hotel_id,
            "status_id": self.status_id,
            "type_id": self.type_id,
            "hotel_name": self.hotel.name,
            "status_name": self.status.status_name,
            "type_name": self.type.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Room:
        obj = Room(**dto_dict)
        return obj
