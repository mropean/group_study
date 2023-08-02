-- 코드를 입력하세요
SELECT
u.USER_ID, u.NICKNAME,
CONCAT(u.CITY," ", u.STREET_ADDRESS1," ", u.STREET_ADDRESS2),
CONCAT(SUBSTR(u.TLNO,1,3), "-", SUBSTR(u.TLNO,4,4), "-", SUBSTR(u.TLNO,8,11))
from
USED_GOODS_USER u,
(
    select
    WRITER_ID
    from
    USED_GOODS_BOARD
    group by
    WRITER_ID
    having
    COUNT(*) >= 3
) as b
where
u.USER_ID = b.WRITER_ID
order by
u.USER_ID desc;