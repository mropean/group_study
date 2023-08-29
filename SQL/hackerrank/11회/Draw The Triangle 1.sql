DELIMITER $$

CREATE PROCEDURE P(IN num INT)
BEGIN
    DECLARE i INT;
    SET i = num;
    
    my_loop: LOOP
        IF i < 1 THEN
            LEAVE my_loop;
        END IF;
    
        SELECT REPEAT("* ", i);

        SET i = i - 1;
  
    END LOOP my_loop;
END$$

DELIMITER ;

CALL P(20);