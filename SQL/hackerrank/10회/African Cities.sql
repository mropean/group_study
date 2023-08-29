with africa_code as (
    select
    CODE
    from
    COUNTRY
    where
    CONTINENT = 'Africa'
)
select
NAME
from
CITY
    inner join
    africa_code
    on
    CITY.COUNTRYCODE = africa_code.CODE