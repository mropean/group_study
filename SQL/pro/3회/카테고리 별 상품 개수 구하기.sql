-- 코드를 입력하세요
SELECT
left(PRODUCT_CODE, 2), COUNT(PRODUCT_CODE)
from
PRODUCT
group by
left(PRODUCT_CODE, 2)
;