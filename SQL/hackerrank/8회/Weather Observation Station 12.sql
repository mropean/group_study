select
DISTINCT(CITY)
from
STATION
where 
CITY REGEXP '^[^aeiou]'
and
CITY REGEXP '[^aeiou]$';