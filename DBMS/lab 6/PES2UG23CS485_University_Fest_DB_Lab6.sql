INSERT INTO participant (SRN, PName, Gender, Department, Semester)
VALUES ('SRN001', 'Test User', 'M', 'CSE', 3);
INSERT INTO item (ItemID, ItemName, Type, Price, StallID, Quantity)
VALUES (1, 'Burger', 'Veg', 100.00, 1, 10);

SELECT * FROM item WHERE ItemID = 1;

DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON purchase
FOR EACH ROW
BEGIN
    UPDATE item
    SET Quantity = Quantity - NEW.Quantity
    WHERE ItemID = NEW.ItemID;
END $$

DELIMITER ;

INSERT INTO purchase (PurchaseID, ParticipantSRN, StallID, ItemID, Quantity, PurchaseTime)
VALUES (201, 'SRN001', 1, 1, 2, NOW());
SELECT * FROM item WHERE ItemID = 1;

SELECT * FROM purchase;

DELIMITER $$

CREATE TRIGGER prevent_large_purchase
BEFORE INSERT ON purchase
FOR EACH ROW
BEGIN
    IF NEW.Quantity > 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Purchase of more than 5 units of a single item is not allowed';
    END IF;
END $$

DELIMITER ;

INSERT INTO purchase (PurchaseID, ParticipantSRN, StallID, ItemID, Quantity, PurchaseTime)
VALUES (301, 'SRN001', 1, 1, 3, NOW());
INSERT INTO purchase (PurchaseID, ParticipantSRN, StallID, ItemID, Quantity, PurchaseTime)
VALUES (302, 'SRN001', 1, 1, 6, NOW());

SELECT * FROM item LIMIT 5;
SELECT * FROM purchase LIMIT 5;

DELIMITER $$

CREATE PROCEDURE GetStallSales(IN input_stall_id INT)
BEGIN
    SELECT i.StallID,
           SUM(i.Price * p.Quantity) AS TotalRevenue
    FROM purchase p
    JOIN item i ON p.ItemID = i.ItemID
    WHERE i.StallID = input_stall_id
    GROUP BY i.StallID;
END $$

DELIMITER ;

CALL GetStallSales(1);

INSERT INTO event_schedule (EventID, EventName, Date_of_conduction, Block, Floor, RoomNo, Price, TeamID)
VALUES (101, 'Test Event', '2025-09-20', 'A', 1, '101', 0.00, NULL);

SELECT * FROM registration LIMIT 5;

DELIMITER $$

CREATE PROCEDURE RegisterParticipant (
    IN p_event_id INT,
    IN p_srn VARCHAR(20),
    IN p_regno INT
)
BEGIN
    INSERT INTO registration (RegNo, EventID, ParticipantSRN)
    VALUES (p_regno, p_event_id, p_srn);
END $$

DELIMITER ;

CALL RegisterParticipant(101, 'SRN001', 5001);
SELECT * FROM registration WHERE RegistrationID = 5001;

SELECT * FROM event_schedule LIMIT 5;

DELIMITER $$

CREATE FUNCTION GetEventCost(input_event_id INT)
RETURNS DECIMAL(6,2)
DETERMINISTIC
BEGIN
    DECLARE event_price DECIMAL(6,2);

    SELECT Price INTO event_price
    FROM event_schedule
    WHERE EventID = input_event_id;

    RETURN event_price;
END $$

DELIMITER ;

SELECT GetEventCost(1) AS EventCost;

SELECT * FROM purchase LIMIT 5;
SELECT * FROM item LIMIT 5;

DELIMITER $$

CREATE FUNCTION GetParticipantPurchaseTotal(input_srn VARCHAR(20))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE total_spent DECIMAL(10,2);

    SELECT SUM(i.Price * p.Quantity) INTO total_spent
    FROM purchase p
    JOIN item i ON p.ItemID = i.ItemID
    WHERE p.ParticipantSRN = input_srn;

    RETURN IFNULL(total_spent, 0);
END $$

DELIMITER ;

SELECT GetParticipantPurchaseTotal('SRN001') AS TotalSpent;
