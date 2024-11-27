from .orders.address_dao import AddressDAO
from .orders.guest_dao import GuestDAO
from .orders.status_dao import StatusDAO
from .orders.reservation_dao import ReservationDAO
from .orders.invoice_guest_dao import InvoiceGuestDAO
from .orders.city_dao import CityDAO
from .orders.hotel_chain_dao import HotelChainDAO
from .orders.invoice_chain_dao import InvoiceChainDAO
from .orders.hotel_dao import HotelDAO
from .orders.type_dao import TypeDAO
from .orders.room_dao import RoomDAO
from .orders.room_reservation_dao import RoomReservationDAO
from .orders.review_dao import ReviewDAO


address_dao = AddressDAO()
guest_dao = GuestDAO()
status_dao = StatusDAO()
reservation_dao = ReservationDAO()
invoice_guest_dao = InvoiceGuestDAO()
city_dao = CityDAO()
hotel_chain_dao = HotelChainDAO()
invoice_chain_dao = InvoiceChainDAO()
hotel_dao = HotelDAO()
type_dao = TypeDAO()
room_dao = RoomDAO()
room_reservation_dao = RoomReservationDAO()
review_dao = ReviewDAO()

