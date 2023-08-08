-- 코드를 입력하세요
SELECT
CART_ID
from
(
    select
    CART_ID, GROUP_CONCAT(DISTINCT NAME) as NAME
    from
    CART_PRODUCTS
    where
    NAME = "Milk"
    or 
    NAME = "Yogurt"
    group by
    CART_ID
) as P1
where
P1.NAME LIKE "%Milk%"
and
P1.NAME LIKE "%Yogurt%"
order by
CART_ID
;