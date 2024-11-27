from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class RoomReservation(db.Model, IDto):
    __tablename__ = "room_reservation"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    discount_percent = db.Column(db.DECIMAL(5,2))
    total_price = db.Column(db.DECIMAL(10,2), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    room = db.relationship("Room", backref="room_reservation")
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    reservation = db.relationship("Reservation", backref="room_reservation")

    def __repr__(self) -> str:
        return f"RoomReservation({self.id},{self.room_id}, '{self.reservation_id}', '{self.discount_percent}', {self.total_price})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "room_id": self.room_id,
            "reservation_id": self.reservation_id,
            "discount_percent": self.discount_percent,
            "total_price": self.total_price,
            "room_name" : self.room.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RoomReservation:
        obj = RoomReservation(**dto_dict)
        return obj
