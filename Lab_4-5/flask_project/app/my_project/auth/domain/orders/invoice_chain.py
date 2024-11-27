from __future__ import annotations
from typing import Dict, Any

from flask_project.app.my_project import db
from flask_project.app.my_project.auth.domain.i_dto import IDto

class InvoiceChain(db.Model, IDto):
    __tablename__ = "invoice_chain"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    amount = db.Column(db.DECIMAL(10,2), nullable=False)
    period = db.Column(db.String(125), nullable=False)
    details = db.Column(db.TEXT(500))
    ts_issued = db.Column(db.TIMESTAMP)
    hotel_chain_id = db.Column(db.Integer, db.ForeignKey('hotel_chain.id'), nullable=False)
    hotel_chain = db.relationship("HotelChain", backref="invoice_chain")

    def __repr__(self) -> str:
        return (f"Invoice_Chain({self.id}, '{self.amount}', '{self.period}', {self.details}, "
                f"{self.ts_issued},  {self.hotel_chain_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "amount": self.amount,
            "period": self.period,
            "details": self.details,
            "ts_issued" : self.ts_issued,
            "hotel_chain_id": self.hotel_chain_id,
            "hotel_chain_name": self.hotel_chain.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InvoiceChain:
        obj = InvoiceChain(**dto_dict)
        return obj
