-- 코드를 입력하세요
SELECT
car.CAR_ID
from
CAR_RENTAL_COMPANY_CAR car,
(
    select
    DISTINCT CAR_ID
    from
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where
    MONTH(START_DATE) = 10
) as history
where
car.CAR_ID = history.CAR_ID
and
car.CAR_TYPE = "세단"
order by
order by
car.CAR_ID desc;