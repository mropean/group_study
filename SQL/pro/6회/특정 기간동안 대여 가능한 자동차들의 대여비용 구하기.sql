-- 코드를 입력하세요
with CAR as (
    SELECT
    C.CAR_ID, C.CAR_TYPE, C.DAILY_FEE 
    from
    CAR_RENTAL_COMPANY_CAR C
        join
        (
            select
            CAR_ID, 
            IF(MAX(START_DATE < '2022-12-01' AND END_DATE >= '2022-11-01'), "대여중", "대여 가능") as AVAILABILITY
            from
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
            group by
            CAR_ID
            order by
            CAR_ID desc
        ) as H
        on
        C.CAR_ID = H.CAR_ID
    where
    H.AVAILABILITY = "대여 가능"
    and
    (
        C.CAR_TYPE = "SUV"
        or
        C.CAR_TYPE = "세단"
    )
),
CAR_TOTAL as (
    select
    C.CAR_ID, C.CAR_TYPE, ROUND((C.DAILY_FEE - (C.DAILY_FEE * (P.DISCOUNT_RATE * 0.01))) * 30) as FEE
    from
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
        join
        CAR C
        on
        P.CAR_TYPE = C.CAR_TYPE
    where
    DURATION_TYPE = "30일 이상"
)

select
*
from
CAR_TOTAL
where
FEE >= 500000
and
FEE < 2000000
order by
FEE desc, CAR_TYPE, CAR_ID desc
;