-- 코드를 입력하세요
SELECT
date_format(DATETIME, "%H") as HOUR, count(*)
from
ANIMAL_OUTS
where
TIME(DATETIME) between "09:00" and "19:59"
group by
HOUR
order by
HOUR
;