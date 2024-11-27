from flask import Flask
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)


    from .orders.address_route import address_bp
    from .orders.guest_route import guest_bp
    from .orders.status_route import status_bp
    from .orders.reservation_route import reservation_bp
    from .orders.invoice_guest_route import invoice_guest_bp
    from .orders.city_route import city_bp
    from .orders.hotel_chain_route import hotel_chain_bp
    from .orders.invoice_chain_route import invoice_chain_bp
    from .orders.hotel_route import hotel_bp
    from .orders.type_route import type_bp
    from .orders.room_route import room_bp
    from .orders.room_reservation_route import room_reservation_bp
    from .orders.review_route import review_bp


    app.register_blueprint(address_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(status_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(invoice_guest_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(hotel_chain_bp)
    app.register_blueprint(invoice_chain_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(type_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(room_reservation_bp)
    app.register_blueprint(review_bp)

