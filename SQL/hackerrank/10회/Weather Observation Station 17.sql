with a as (
    select
    MIN(LAT_N) as LAT_N
    from
    STATION
    where
    LAT_N > 38.7780 
)

select
ROUND(LONG_W, 4)
from
STATION
    inner join
    a
    on
    STATION.LAT_N = a.LAT_N
    