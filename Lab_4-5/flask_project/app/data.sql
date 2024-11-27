USE `lab4db`;

INSERT INTO type (name) VALUES
('Standard'),
('Deluxe'),
('Suite'),
('Family Room'),
('Executive');

INSERT INTO status (status_name) VALUES
("Checked-in"),
("Checked-out"),
("Cancelled"),
("Booked"),
("Available"),
("Overbooked");

INSERT INTO address (street, house_number) VALUES
("Main St", 123),
("Elm St", 456),
("Oak Ave", 789),
("Pine St", 101),
("Maple St", 206),
("Cedar Ave", 346),
("Birch St", 9),
("Walnut St", 11),
("Cherry Ln", 678),
("Spruce St", 22),
("Willow St", 55),
("Poplar Ave", 1678),
("Ash St", 1134),
("Redwood St", 226),
("Cypress Ln", 85);

INSERT INTO city (name) VALUES
("Rio de Janeiro"),
("Lviv"),
("Ternopil"),
("London"),
("Tokyo"),
("Paris"),
("Dubai"),
("Las Vegas"),
("New York City"),
("Rome");

INSERT INTO hotel_chain (name, vat_id, email, city_id, main_address, details, is_active) VALUES
("Luxury Resorts International", "LRI123456789", "info@luxuryresorts.com", 1, "1127 Oceanfront Drive", "High-end resort chain with beachfront properties worldwide", 1),
("Cozy Inn Group", "CIG987654321", "reservations@cozyinn.com", 3, "361 Main Street", "Budget-friendly hotels perfect for family vacations and business trips", 1),
("Metropolitan Hotels", "MH456789123", "contact@metrohotels.com", 5, "58 City Center Blvd", "Upscale urban hotels catering to business travelers and tourists", 1),
("EcoStay Lodges", "ESL159753468", "bookings@ecostay.com", 4, "4101 Green Valley Road", "Environmentally friendly accommodations in natural settings", 0),
("Heritage Inns & Suites", "HIS753951852", "stay@heritageinns.com", 5, "523 Historic Square", "Boutique hotels in restored historic buildings", 1),
("Global Suites Network", "GSN369258147", "global@suitesnetwork.com", 6,"6923 International Plaza", "Extended stay suites for long-term travelers and relocations", 1),
("Alpine Retreat Collection", "ARC147258369", "reservations@alpineretreats.com", 7, "7489 Mountain View Drive", "Luxury ski resorts and mountain lodges", 1),
("Seaside Bed & Breakfast Chain", "SBB951753852", "info@seasidebb.com", 8,"8469 Coastal Highway", "Charming B&Bs in picturesque coastal towns", 0),
("TechnoStay Hotels", "TSH753159852", "support@technostay.com", 2, "2676 Silicon Valley Way", "High-tech hotels with cutting-edge amenities for tech-savvy guests", 1),
("Wellness Oasis Resorts", "WOR258369147", "relax@wellnessoasis.com", 2, "278 Tranquility Lane", "Health-focused resorts offering spa treatments and wellness programs", 1);

INSERT INTO invoice_chain (hotel_chain_id, amount, period, details, ts_issued) VALUES
(1, "1200.50", "2024-Q1", "Invoice for Q1 operations", "2024-04-01 09:30:00"),
(2, "2300.75", "2024-Q1", "Invoice for Q1 operations", "2024-04-02 10:00:00"),
(3, "1400.20", "2024-Q2", "Invoice for Q2 operations", "2024-07-01 08:45:00"),
(4, "3250.00", "2024-Q1", "Invoice for Q1 operations", "2024-04-03 11:15:00"),
(5, "2750.40", "2024-Q1", "Invoice for Q1 operations", "2024-04-05 12:00:00"),
(6, "3400.85", "2024-Q2", "Invoice for Q2 operations", "2024-07-01 09:15:00"),
(7, "4500.10", "2024-Q2", "Invoice for Q2 operations", "2024-07-03 10:30:00"),
(8, "2600.35", "2024-Q2", "Invoice for Q2 operations", "2024-07-05 11:45:00"),
(9, "1500.60", "2024-Q1", "Invoice for Q1 operations", "2024-04-06 13:00:00"),
(1, "01750.80", "2024-Q2", "Invoice for Q2 operations", "2024-07-07 14:15:00");

INSERT INTO hotel (hotel_chain_id, city_id, name, description, is_active) VALUES
(1, 9, "Luxury Resorts New York", "Upscale hotel in the heart of Manhattan", 1),
(1, 6, "Luxury Resorts Paris", "Elegant accommodation near the Eiffel Tower", 1),
(2, 4, "Cozy Inn London", "Affordable comfort in central London", 1),
(2, 5, "Cozy Inn Tokyo", "Budget-friendly stay in bustling Tokyo", 1),
(3, 10, "Metropolitan Rome", "Modern luxury in the Eternal City", 1),
(3, 7, "Metropolitan Dubai", "Sleek high-rise in downtown Dubai", 1),
(4, 3, "EcoStay Hong Ternopil", "Sustainable living in urban Hong Kong", 0),
(4, 8, "EcoStay Las Vegas", "Green oasis in the heart of Singapore", 0),
(5, 2, "Heritage Lviv", "Historic charm meets modern comfort", 1),
(6, 1, "Global Suites Rio", "Long-stay comfort with breathtaking views", 0),
(7, 9, "Alpine Retreat NYC", "Mountain lodge feel in the big city", 1),
(8, 6, "Seaside B&B Paris", "Parisian charm with a coastal theme", 0),
(9, 4, "TechnoStay London", "Cutting-edge amenities for the tech-savvy traveler", 1),
(10, 5, "Wellness Oasis Tokyo", "Urban retreat focused on health and relaxation", 1),
(5, 9, "Heritage New York City", "Boutique hotel with views of ancient Rome", 1);

INSERT INTO room (name, description, price, hotel_id, status_id, type_id) VALUES
("101", "Cozy standard room with city view", "150.00", 1, 1, 1),
("201", "Spacious deluxe room with king bed", "250.00", 1, 2, 2),
("Executive Suite", "Luxurious suite with separate living area", "500.00", 2, 1, 3),
("Family Room", "Large room with two queen beds", "300.00", 3, 6, 4),
("301", "Standard room with efficient layout", "100.00", 4, 1, 1),
("Panorama Suite", "Top floor suite with breathtaking views", "800.00", 5, 1, 3),
("501", "Modern deluxe room with smart features", "400.00", 6, 2, 2),
("Eco Room", "Sustainable room with bamboo furnishings", "200.00", 7, 1, 1),
("Garden View", "Deluxe room overlooking lush gardens", "350.00", 8, 6, 2),
("Heritage Suite", "Elegant suite with antique decor", "600.00", 9, 1, 3),
("Long Stay Studio 001", "Compact studio with kitchenette", "180.00", 10, 2, 1),
("Mountain View Room", "Room with faux mountain cabin decor", "280.00", 11, 1, 2),
("Parisian Loft 5", "Charming attic room with exposed beams", "220.00", 12, 6, 1),
("Tech Suite 99", "High-tech suite with latest gadgets", "550.00", 13, 1, 5),
("Zen Deluxe", "Calming room with minimalist design", "320.00", 14, 6, 2);

INSERT INTO guest (name, surname, email, phone, details, address_id) VALUES
("John", "Doe", "john.doe@gmail.com", "+1234567890", "VIP Guest", 1),
("Jane", "Smith", "jane.smith@gmail.com", "+0987654321", "Returning customer", 2),
("Michael", "Johnson", "michael.j@gmail.com", "+1122334455", "Preferred guest", 3),
("Emily", "Brown", "emily.brown@gmail.com", "+9988776655", "First-time guest", 4),
("David", "Taylor", "david.t@gmail.com", "+4455667788", "Frequent traveler", 5),
("Sophia", "Miller", "sophia.m@gmail.com", "+3344556677", "Business traveler", 6),
("James", "Wilson", "james.w@gmail.com", "+7788990011", "Conference attendee", 7),
("Olivia", "Moore", "olivia.moore@gmail.com", "+6677889900", "Long-term stay", 8),
("Robert", "Davis", "robert.d@gmail.com", "+5566778899", "International traveler", 9),
("Lucas", "Anderson", "lucas.a@gmail.com", "+4455778899", "Seasonal guest", 10),
("Isabella", "White", "isabella.w@gmail.com", "+3344667788", "Honeymoon stay", 11),
("Ethan", "Thomas", "ethan.t@gmail.com", "+2233445566", "Budget traveler", 12),
("Mia", "Jackson", "mia.j@gmail.com", "+1122446688", "Family vacation", 13);


INSERT INTO reservation (guest_id, start_date, end_date, ts_created, ts_updated, status_id) VALUES
(1, "2024-10-01", "2024-10-05", "2024-09-20 12:00:00", "2024-09-21 12:00:00", 1),
(2, "2024-10-10", "2024-10-12", "2024-09-21 13:00:00", "2024-09-22 13:00:00", 2),
(3, "2024-10-15", "2024-10-20", "2024-09-23 14:00:00", "2024-09-24 14:00:00", 2),
(4, "2024-10-05", "2024-10-07", "2024-09-25 15:00:00", "2024-09-26 15:00:00", 2),
(5, "2024-11-01", "2024-11-05", "2024-09-26 16:00:00", "2024-09-27 16:00:00", 1),
(6, "2024-11-10", "2024-11-15", "2024-09-27 17:00:00", "2024-09-28 17:00:00", 1),
(7, "2024-11-20", "2024-11-22", "2024-09-28 18:00:00", "2024-09-29 18:00:00", 3),
(9, "2024-12-05", "2024-12-10", "2024-10-01 12:00:00", "2024-10-02 12:00:00", 3),
(10, "2024-12-15", "2024-12-20", "2024-10-03 13:00:00", "2024-10-04 13:00:00", 3),
(1, "2025-01-10", "2025-01-15", "2024-10-08 17:00:00", "2024-10-09 17:00:00", 1),
(2, "2025-01-20", "2025-01-25", "2024-10-09 18:00:00", "2024-10-10 18:00:00", 2),
(4, "2025-01-20", "2025-01-25", "2024-10-09 18:00:00", "2024-10-10 18:00:00", 1);

INSERT INTO room_reservation (room_id, reservation_id, discount_percent, total_price) VALUES
(1, 1, 5.00, 500.00),
(2,	2, 10.00, 750.00),
(3,	3, 0.00, 1200.00),
(4,	4, 5.00, 600.00),
(5,	5, 0.00, 1000.00),
(6,	6, 15.00, 1300.00),
(7,	7, 0.00, 500.00),
(8,	9, 10.00, 600.00),
(9,	9, 0.00, 1250.00),
(10, 10, 5.00,1500.00),
(11, 11, 20.00, 2000.00),
(11, 12, 0.00, 4354.00),
(12, 5, 5.00, 1800.00),
(13, 9, 0.00, 2200.00),
(14, 11, 10.00, 1750.00),
(15, 5, 0.00, 1600.00);

INSERT INTO invoice_guest (guest_id, amount, ts_issued, reservation_id) VALUES
(1, "500.00", "2024-10-01 10:00:00", 1),
(2, "750.00", "2024-10-10 11:00:00", 2),
(3, "1200.00", "2024-10-15 12:00:00", 3),
(4, "600.00", "2024-10-05 13:00:00", 4),
(5, "1000.00", "2024-11-01 14:00:00", 5),
(6, "1300.00", "2024-11-10 15:00:00", 6),
(7, "500.00", "2024-11-20 16:00:00", 7),
(8, "600.00", "2024-12-01 17:00:00", 8),
(9, "1250.00", "2024-12-05 18:00:00", 9),
(10, "1500.00", "2024-12-15 19:00:00", 10),
(11, "2000.00", "2024-12-22 20:00:00", 11);
