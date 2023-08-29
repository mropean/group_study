select
ROUND(a.LAT_N, 4)
from
(
    select
    LAT_N
    from
    STATION
    order by
    LAT_N
    limit 250
) as a
order by
a.LAT_N desc
limit 1
--
DELIMITER //

-- CREATE PROCEDURE GetDynamicLimitedValue()
-- BEGIN
--     DECLARE dynamic_limit INT;
--     SELECT COUNT(LAT_N) INTO dynamic_limit FROM STATION;

--     IF dynamic_limit % 2 = 0 THEN
--         SET dynamic_limit = FLOOR(dynamic_limit / 2);
--         SET @sql_query = CONCAT('SELECT AVG(sub.LAT_N)
--                                  FROM (SELECT LAT_N
--                                        FROM STATION
--                                        ORDER BY LAT_N
--                                        LIMIT ', dynamic_limit - 1, ', 2) as sub;');
--     ELSE
--         SET dynamic_limit = FLOOR((dynamic_limit + 1) / 2);
--         SET @sql_query = CONCAT('SELECT ROUND(a.LAT_N, 4)
--                                  FROM (SELECT LAT_N
--                                        FROM STATION
--                                        ORDER BY LAT_N
--                                        LIMIT ', dynamic_limit, ') as a
--                                  ORDER BY a.LAT_N DESC
--                                  LIMIT 1;');
--     END IF;

--     PREPARE dynamic_query FROM @sql_query;
--     EXECUTE dynamic_query;
--     DEALLOCATE PREPARE dynamic_query;
-- END;
-- //

-- DELIMITER ;

-- CALL GetDynamicLimitedValue();
