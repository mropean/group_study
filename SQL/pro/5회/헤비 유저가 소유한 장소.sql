-- 코드를 입력하세요
SELECT
P1.ID, P1.NAME, P1.HOST_ID
from
PLACES P1
    join
    (
        select
        HOST_ID, COUNT(*)
        from
        PLACES
        group by
        HOST_ID
        having
        COUNT(*) > 1
    ) as P2
    on
    P1.HOST_ID = P2.HOST_ID
order by
P1.ID
;