-- 코드를 입력하세요
SELECT
MONTH(C2.START_DATE), C2.CAR_ID, COUNT(*) as RECORDS
from
CAR_RENTAL_COMPANY_RENTAL_HISTORY C2
    join
    (
        select
        CAR_ID
        from
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where
        START_DATE > "2022-07-31"
        and
        START_DATE < "2022-11-01"
        group by
        CAR_ID
        having
        COUNT(*) > 4
    ) as C1
    on
    C1.CAR_ID = C2.CAR_ID
where
C2.START_DATE > "2022-07-31"
and
C2.START_DATE < "2022-11-01"
group by
MONTH(C2.START_DATE), C2.CAR_ID
having
COUNT(*) > 0
order by
MONTH(C2.START_DATE), C2.CAR_ID desc
;