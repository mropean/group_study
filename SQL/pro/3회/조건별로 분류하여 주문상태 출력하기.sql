-- 코드를 입력하세요
SELECT
ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, "%Y-%m-%d"),
    CASE
        WHEN (OUT_DATE IS NULL) THEN "출고미정"
        WHEN (date_format(OUT_DATE, "%Y-%m-%d") > "2022-05-01" ) THEN "출고대기"
        ELSE "출고완료"
    END
from
FOOD_ORDER
order by
ORDER_ID;