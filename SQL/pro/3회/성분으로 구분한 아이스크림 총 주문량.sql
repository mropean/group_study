-- 코드를 입력하세요
SELECT
INGREDIENT_TYPE, SUM(TOTAL_ORDER) as "TOTAL_ORDER"
from
FIRST_HALF
    inner join
    ICECREAM_INFO
    on
    FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
group by
INGREDIENT_TYPE
having
SUM(TOTAL_ORDER)
order by
SUM(TOTAL_ORDER);