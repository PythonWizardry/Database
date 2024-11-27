from .orders.address_service import AddressService
from .orders.guest_service import GuestService
from .orders.status_service import StatusService
from .orders.reservation_service import ReservationService
from .orders.invoice_guest_service import InvoiceGuestService
from .orders.city_service import CityService
from .orders.hotel_chain_service import HotelChainService
from .orders.invoice_chain_service import InvoiceChainService
from .orders.hotel_service import HotelService
from .orders.type_service import TypeService
from .orders.room_service import RoomService
from .orders.room_reservation_servive import RoomReservationService
from .orders.review_service import ReviewService


address_service = AddressService()
guest_service = GuestService()
status_service = StatusService()
reservation_service = ReservationService()
invoice_guest_service = InvoiceGuestService()
city_service = CityService()
hotel_chain_service = HotelChainService()
invoice_chain_service = InvoiceChainService()
hotel_service = HotelService()
type_service = TypeService()
room_service = RoomService()
room_reservation_service = RoomReservationService()
review_service = ReviewService()

