from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class InvoiceGuest(db.Model, IDto):
    __tablename__ = "invoice_guest"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    guest = db.relationship("Guest", backref="invoice_guest")
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    reservation = db.relationship("Reservation", backref="invoice_guest")
    amount = db.Column(db.DECIMAL(10,2), nullable=False)
    ts_issued = db.Column(db.TIMESTAMP, nullable=False)


    def __repr__(self) -> str:
        return f"InvoiceGuest({self.id}, '{self.guest_id}', '{self.reservation_id}', {self.ts_issued})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "guest_id": self.guest_id,
            "reservation_id": self.reservation_id,
            "amount": self.amount,
            "ts_issued": self.ts_issued
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InvoiceGuest:
        obj = InvoiceGuest(**dto_dict)
        return obj
