USE lab4db;

DROP PROCEDURE IF EXISTS get_guest_after_address_id;
DELIMITER //
CREATE PROCEDURE get_guest_after_address_id(IN address_id INT)
BEGIN
SELECT adr.street, g.name, g.surname
FROM address adr
JOIN guest g ON g.address_id = adr.id
WHERE adr.id = address_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_reservation_after_guest;
DELIMITER //
CREATE PROCEDURE get_reservation_after_guest(IN guest_id INT)
BEGIN
SELECT res.id reservation_id, res.ts_created created, g.name guest_name
FROM reservation res
JOIN invoice_guest ing ON res.id = ing.reservation_id
JOIN guest g ON g.id = ing.guest_id
WHERE ing.guest_id = guest_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_guest_after_reservation;
DELIMITER //
CREATE PROCEDURE get_guest_after_reservation(IN reservation_id INT)
BEGIN
SELECT g.id guest_id, g.name name, g.surname surname, adr.street
FROM guest g
JOIN invoice_guest ing ON g.id = ing.reservation_id
JOIN address adr ON adr.id = ing.guest_id
WHERE ing.reservation_id = reservation_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_reservation_after_guest_id;
DELIMITER //
CREATE PROCEDURE get_reservation_after_guest_id(IN guest_id INT)
BEGIN
SELECT res.id, res.start_date, res.end_date, g.name, g.surname
FROM guest g
JOIN reservation res ON res.guest_id = g.id
WHERE g.id = guest_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_reservation_after_status_id;
DELIMITER //
CREATE PROCEDURE get_reservation_after_status_id(IN status_id INT)
BEGIN
SELECT res.id, res.start_date, res.end_date, st.status_name
FROM status st
JOIN reservation res ON res.status_id = st.id
WHERE st.id = status_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_room_after_status_id;
DELIMITER //
CREATE PROCEDURE get_room_after_status_id(IN status_id INT)
BEGIN
SELECT rm.id, rm.name, rm.price, st.status_name
FROM status st
JOIN room rm ON rm.status_id = st.id
WHERE st.id = status_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_room_after_hotel_id;
DELIMITER //
CREATE PROCEDURE get_room_after_hotel_id(IN hotel_id INT)
BEGIN
SELECT ht.id, ht.name, rm.name, ht.is_active
FROM hotel ht
JOIN room rm ON rm.hotel_id = ht.id
JOIN city c ON ht.city_id = c.id
WHERE ht.id = hotel_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_room_after_type_id;
DELIMITER //
CREATE PROCEDURE get_room_after_type_id(IN type_id INT)
BEGIN
SELECT tp.id, tp.name, rm.name, rm.price
FROM type tp
JOIN room rm ON rm.type_id = tp.id
WHERE tp.id = type_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_room_after_reservation;
DELIMITER //
CREATE PROCEDURE get_room_after_reservation(IN reservation_id INT)
BEGIN
SELECT rm.id, rm.name, tp.name, rm.price
FROM room rm
JOIN room_reservation ing ON rm.id = ing.room_id
JOIN type tp ON tp.id = rm.type_id
JOIN status st ON st.id = rm.status_id
WHERE ing.reservation_id = reservation_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_reservation_after_room;
DELIMITER //
CREATE PROCEDURE get_reservation_after_room(IN room_id INT)
BEGIN
SELECT res.id, res.start_date, res.end_date, g.name, st.status_name
FROM reservation res
JOIN room_reservation ing ON res.id = ing.reservation_id
JOIN guest g ON g.id = res.guest_id
JOIN status st ON st.id = res.status_id
WHERE ing.room_id = room_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_hotel_after_hotel_chain_id;
DELIMITER //
CREATE PROCEDURE get_hotel_after_hotel_chain_id(IN hotel_chain_id INT)
BEGIN
SELECT ht.id, ht.name, ht.is_active, city.name
FROM hotel_chain htc
JOIN hotel ht ON ht.hotel_chain_id = htc.id
JOIN city ON city.id = ht.city_id
WHERE htc.id = hotel_chain_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_hotel_after_city_id;
DELIMITER //
CREATE PROCEDURE get_hotel_after_city_id(IN city_id INT)
BEGIN
SELECT ht.id, ht.name, ht.is_active
FROM city c
JOIN hotel ht ON ht.city_id = c.id
WHERE c.id = city_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_hotel_chain_after_city_id;
DELIMITER //
CREATE PROCEDURE get_hotel_chain_after_city_id(IN city_id INT)
BEGIN
SELECT htc.id, htc.name, htc.main_address, htc.email
FROM city c
JOIN hotel_chain htc ON htc.city_id = c.id
WHERE c.id = city_id;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS get_invoice_chain_after_hotel_chain_id;
DELIMITER //
CREATE PROCEDURE get_invoice_chain_after_hotel_chain_id(IN hotel_chain_id INT)
BEGIN
SELECT inc.id, inc.amount, inc.period
FROM hotel_chain htc
JOIN invoice_chain inc ON inc.hotel_chain_id = htc.id
WHERE htc.id = hotel_chain_id;
END //
DELIMITER ;





-- For Lab 5
DROP TRIGGER IF EXISTS insert_fk;
DROP TRIGGER IF EXISTS update_fk;
DROP TRIGGER IF EXISTS delete_fk;




DELIMITER //

CREATE TRIGGER insert_fk
BEFORE INSERT ON review
FOR EACH ROW
BEGIN
    DECLARE guest_exists INT;
    SELECT COUNT(*) INTO guest_exists FROM guest WHERE id = NEW.guest_id;
    IF guest_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hm, Guest does not exist';
    END IF;
END //


CREATE TRIGGER update_fk
BEFORE UPDATE ON review
FOR EACH ROW
BEGIN
    DECLARE guest_exists INT;
    SELECT COUNT(*) INTO guest_exists FROM guest WHERE id = NEW.guest_id;
    IF guest_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hm, Guest does not exist.';
    END IF;
END //


CREATE TRIGGER delete_fk
BEFORE DELETE ON guest
FOR EACH ROW
BEGIN
    DECLARE guest_count INT;
    SELECT COUNT(*) INTO guest_count FROM review WHERE guest_id = OLD.id;
    IF guest_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete this Guest.';
    END IF;
END //

DELIMITER ;

-- examples
-- INSERT INTO review (guest_id, review_context) VALUES (1, 'Great experience!');
-- INSERT INTO review (guest_id, review_context) VALUES (999, 'Terrible service.');

-- UPDATE review SET guest_id = 20 WHERE id = 3;
-- UPDATE review SET guest_id = 999 WHERE id = 3;

-- INSERT INTO	guest (name, surname, email, address_id) VALUES("Yulia", "Tumoshenko", "can'tcomeupwith@gamil.com", 5);
-- DELETE FROM guest WHERE id = 16;
-- INSERT INTO	guest (name, surname, email, address_id) VALUES("Yulia", "Tumoshenko", "can'tcomeupwith@gamil.com", 5);
-- INSERT INTO review (guest_id, review_context) VALUES (20, 'Yushchenko, YES!');
-- DELETE FROM guest WHERE id = 20;



DROP PROCEDURE IF EXISTS insert_into_review;
DELIMITER //
CREATE PROCEDURE insert_into_review(
IN guest_id INT,
IN review_context TEXT(250)
)
BEGIN
INSERT INTO review (guest_id, review_context)
VALUES (guest_id, review_context);
END//
DELIMITER ;

-- CALL insert_into_review(3, "Potatoes is good here ")




DROP PROCEDURE IF EXISTS insert_into_room_reservation;
DELIMITER //
CREATE PROCEDURE insert_into_room_reservation(
    IN room_name VARCHAR(45),
    IN reservation_created TIMESTAMP,
    IN discount_percent DECIMAL(5,2),
    IN total_price DECIMAL(10,2)
)
BEGIN
    DECLARE room_id INT;
    DECLARE reservation_id INT;

    SELECT id INTO room_id
    FROM room
    WHERE name = room_name;

    IF room_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Room does not exist';
    END IF;

    SELECT id INTO reservation_id
    FROM reservation
    WHERE ts_created = reservation_created;

    IF reservation_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Reservation does not exist';
    END IF;

    INSERT INTO room_reservation (room_id, reservation_id, discount_percent, total_price)
    VALUES (room_id, reservation_id, discount_percent, total_price);
END //

DELIMITER ;

-- call insert_into_room_reservation("101", "2024-09-25 15:00:00", 2.50, 780.37)


DROP PROCEDURE IF EXISTS package_insert;
DELIMITER //
CREATE PROCEDURE package_insert()
BEGIN
    DECLARE num INT DEFAULT 1;
    WHILE num <= 10 DO
        INSERT INTO city (name)
        VALUE (CONCAT('UndefinedCity', num));
        SET num = num + 1;
    END WHILE;
END //
DELIMITER ;


DROP FUNCTION IF EXISTS calculate_invoice_chain;
DELIMITER //
CREATE FUNCTION calculate_invoice_chain(type VARCHAR(10))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(10, 2);

    IF type = 'max' THEN
        SELECT MAX(amount) INTO result FROM invoice_chain;
    ELSEIF type = 'min' THEN
        SELECT MIN(amount) INTO result FROM invoice_chain;
    ELSEIF type = 'sum' THEN
        SELECT SUM(amount) INTO result FROM invoice_chain;
    ELSEIF type = 'avg' THEN
        SELECT AVG(amount) INTO result FROM invoice_chain;
    END IF;

    RETURN result;
END //

DROP PROCEDURE IF EXISTS procedure_calculate_invoice_chain//
CREATE PROCEDURE procedure_calculate_invoice_chain(type VARCHAR(10))
BEGIN
    SELECT calculate_invoice_chain(type) AS result;
END //
DELIMITER ;

-- call procedure_calculate_invoice_chain("sum")


DROP DATABASE IF EXISTS for_cur;
CREATE DATABASE for_cur;
USE for_cur;

DROP PROCEDURE IF EXISTS create_tables;

DELIMITER //

CREATE PROCEDURE create_tables()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE status_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM lab4db.status;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO status_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET @current_timestamp = DATE_FORMAT(NOW(), '%Y%m%d%H%i%s');
        SET @table_name = CONCAT('status_', status_id, '_', @current_timestamp);
        SET @num_columns = FLOOR(1 + (RAND() * 9));
        SET @columns = '';

        SET @i = 1;
        WHILE @i <= @num_columns DO
            SET @column_name = CONCAT('col', @i);
            SET @column_type = 'INT';
            SET @columns = CONCAT(@columns, @column_name, ' ', @column_type, IF(@i < @num_columns, ', ', ''));
            SET @i = @i + 1;
        END WHILE;

        SET @create_table_sql = CONCAT('CREATE TABLE ', @table_name, ' (id INT AUTO_INCREMENT PRIMARY KEY, ', @columns, ')');
        PREPARE stmt FROM @create_table_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

    END LOOP;

    CLOSE cur;
END //

DELIMITER ;

-- CALL create_tables();


DROP TRIGGER IF EXISTS insert_not_allowed;
DELIMITER //
CREATE TRIGGER insert_not_allowed
BEFORE INSERT ON status
FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Updates are not allowed';
END //


DROP TRIGGER IF EXISTS update_not_allowed;
CREATE TRIGGER update_not_allowed
BEFORE UPDATE ON status
FOR EACH ROW
BEGIN
	SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Updates are not allowed';
END //

DROP TRIGGER IF EXISTS insert_apartment_number
CREATE TRIGGER insert_apartment_number
BEFORE INSERT ON address
FOR EACH ROW
BEGIN
    IF NEW.apartment_number NOT REGEXP '^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid apartment_name format.';
    END IF;
END //

DROP TRIGGER IF EXISTS update_apartment_number
CREATE TRIGGER update_apartment_number
BEFORE UPDATE ON address
FOR EACH ROW
BEGIN
    IF NEW.apartment_number NOT REGEXP '^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid apartment_name format.';
    END IF;
END //


DROP TRIGGER IF EXISTS insert_into_room;
CREATE TRIGGER insert_into_room
BEFORE INSERT ON room
FOR EACH ROW
BEGIN
DECLARE row_count INT;
SELECT COUNT(*) INTO row_count FROM room;
IF row_count >=20 3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Maximum 20 rows. I can`t insert more rows';
END IF;
END//

DROP TRIGGER IF EXISTS delete_from_room;
CREATE TRIGGER delete_from_room
BEFORE DELETE ON room
FOR EACH ROW
BEGIN
DECLARE row_count INT;
SELECT COUNT(*) INTO row_count FROM room;
IF row_count <= 15 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Minimum 15 rows. I can`t delete more rows';
END IF;
END//


DELIMITER ;