from .orders.address_controller import AddressController
from .orders.guest_controller import GuestController
from .orders.status_controller import StatusController
from .orders.reservation_controller import ReservationController
from .orders.invoice_guest_controller import InvoiceGuestController
from .orders.city_controller import CityController
from .orders.hotel_chain_controller import HotelChainController
from .orders.invoice_chain_controller import InvoiceChainController
from .orders.hotel_controller import HotelController
from .orders.type_controller import TypeController
from .orders.room_controller import RoomController
from .orders.room_reservation_controller import RoomReservationController
from .orders.review_controller import ReviewController


address_controller = AddressController()
guest_controller = GuestController()
status_controller = StatusController()
reservation_controller = ReservationController()
invoice_guest_controller = InvoiceGuestController()
city_controller = CityController()
hotel_chain_controller = HotelChainController()
invoice_chain_controller = InvoiceChainController()
hotel_controller = HotelController()
type_controller = TypeController()
room_controller = RoomController()
room_reservation_controller = RoomReservationController()
review_controller = ReviewController()

