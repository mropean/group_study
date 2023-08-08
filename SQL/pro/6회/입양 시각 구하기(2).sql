-- 코드를 입력하세요
with RECURSIVE time(HOUR) as (
    select 0
    union all
    select
    HOUR + 1
    from
    time
    where
    HOUR < 23
),
table_data as (
    select
    hour(DATETIME) as HOUR, COUNT(*) as CNT
    from
    ANIMAL_OUTS
    group by
    hour(DATETIME)
)

select
time.HOUR, IFNULL(table_data.CNT, 0)
from
time
    left join
    table_data
    on
    time.HOUR = table_data.HOUR
    ;