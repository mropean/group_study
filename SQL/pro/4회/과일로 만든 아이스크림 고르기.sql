-- 코드를 입력하세요
SELECT
half.FLAVOR
from
FIRST_HALF half
    inner join
    (
        select
        *
        from
        ICECREAM_INFO
        where
        INGREDIENT_TYPE = "fruit_based"
    ) as info
    on
    half.FLAVOR = info.FLAVOR
where
half.TOTAL_ORDER > 3000
order by
half.TOTAL_ORDER desc
;