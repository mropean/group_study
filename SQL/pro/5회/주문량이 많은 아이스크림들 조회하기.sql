-- 코드를 입력하세요
with total as(
    select 
    F.FLAVOR, F.TOTAL_ORDER + COALESCE(SUM(J.TOTAL_ORDER), 0) AS TOTAL_ORDER
    from
    FIRST_HALF F
        join
        JULY J
        on
        F.FLAVOR = J.FLAVOR
    group by
    F.FLAVOR
)

SELECT
FLAVOR
from
total
order by
TOTAL_ORDER desc
limit 3;