with nameLength as (
    select
    CITY, LENGTH(CITY) as "len"
    from
    STATION
    order by
    LENGTH(CITY), CITY
)

(select
*
from
nameLength
where
    len = (select
            MIN(len)
            from
            nameLength)
order by
CITY
limit 1)
UNION ALL
(select
*
from
nameLength
where
    len = (select
            MAX(len)
            from
            nameLength)
order by
CITY
limit 1);