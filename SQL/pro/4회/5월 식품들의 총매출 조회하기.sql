-- 코드를 입력하세요
SELECT
p1.PRODUCT_ID, p1.PRODUCT_NAME, p1.PRICE * o1.AMOUNT
from
FOOD_PRODUCT p1
    inner join
        (
            select
            PRODUCT_ID, SUM(AMOUNT) as "AMOUNT"
            from
            FOOD_ORDER
            where
            YEAR(PRODUCE_DATE) = 2022
            and
            MONTH(PRODUCE_DATE) = 5
            group by
            PRODUCT_ID
        ) as o1
    on
    p1.PRODUCT_ID = o1.PRODUCT_ID
order by
p1.PRICE * o1.AMOUNT desc, p1.PRODUCT_ID
;