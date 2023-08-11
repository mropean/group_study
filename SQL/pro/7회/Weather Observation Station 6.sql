select
DISTINCT(CITY)
from
STATION
where 
-- CITY LIKE 'a%' or 
-- CITY LIKE 'e%' or 
-- CITY LIKE 'i%' or 
-- CITY LIKE 'o%' or 
-- CITY LIKE 'u%'
CITY REGEXP '^[aeiou]'