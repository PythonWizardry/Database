from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class Reservation(db.Model, IDto):
    __tablename__ = "reservation"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    guest = db.relationship("Guest", backref="reservation")
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    status = db.relationship("Status", backref="reservation")
    start_date = db.Column(db.DATE, nullable=False)
    end_date = db.Column(db.DATE, nullable=False)
    ts_created = db.Column(db.TIMESTAMP, nullable=False)
    ts_updated = db.Column(db.TIMESTAMP, nullable=False)

    def __repr__(self) -> str:
        return (f"Reservation({self.id}, '{self.guest_id}', '{self.status_id}', {self.start_date}, "
                f"{self.end_date}, {self.ts_created}, {self.ts_updated})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "guest_id":self.guest_id,
            "status_id":self.status_id,
            "start_date": self.start_date,
            "end_date":self.end_date,
            "ts_created": self.ts_created,
            "ts_updated":self.ts_updated
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reservation:
        obj = Reservation(**dto_dict)
        return obj
