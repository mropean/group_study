-- 코드를 입력하세요
SELECT
P1.CATEGORY, P1.PRICE, P1.PRODUCT_NAME
from
FOOD_PRODUCT P1,
(
    select
    CATEGORY, MAX(PRICE) as "PRICE"
    from
    FOOD_PRODUCT
    where
    CATEGORY in ("과자", "국", "김치", "식용유")
    group by
    CATEGORY
) as P2
where
P1.CATEGORY = P2.CATEGORY
and
P1.PRICE = P2.PRICE
order by
P1.PRICE desc;