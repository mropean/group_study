with asia_code as (
    select
    CODE
    from
    COUNTRY
    where
    CONTINENT = 'Asia'
)
select
SUM(POPULATION)
from
CITY
    inner join
    asia_code
    on
    CITY.COUNTRYCODE = asia_code.CODE