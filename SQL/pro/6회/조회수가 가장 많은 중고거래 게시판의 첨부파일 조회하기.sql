-- 코드를 입력하세요
with test as (
SELECT
BOARD_ID
from
USED_GOODS_BOARD
order by
VIEWS desc
limit 1
)

select
CONCAT("/home/grep/src/",F.BOARD_ID,"/",FILE_ID,FILE_NAME, FILE_EXT)
from
USED_GOODS_FILE F
    join
    test
    on
    F.BOARD_ID = test.BOARD_ID
order by
FILE_ID desc;