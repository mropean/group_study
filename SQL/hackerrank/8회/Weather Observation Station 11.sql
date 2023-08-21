select
DISTINCT(CITY)
from
STATION
where 
CITY REGEXP '^[^aeiou]'
or
CITY REGEXP '[^aeiou]$';