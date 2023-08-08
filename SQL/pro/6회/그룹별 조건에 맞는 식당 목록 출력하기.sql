-- 코드를 입력하세요
with review_counts as (
    SELECT
    MEMBER_ID, COUNT(*) as R_COUNT
    from
    REST_REVIEW
    group by
    MEMBER_ID
    order by
    R_COUNT desc
),
TOP_MEMBER as (
    select
    MEMBER_ID
    from
    review_counts
    where
    R_COUNT = (
                select
                MAX(R_COUNT)
                from
                review_counts
              )
)

select
P.MEMBER_NAME, R.REVIEW_TEXT, date_format(R.REVIEW_DATE, "%Y-%m-%d")
from
REST_REVIEW R
    join
    MEMBER_PROFILE P
    on
    R.MEMBER_ID = P.MEMBER_ID
    join
    TOP_MEMBER T
    on
    R.MEMBER_ID = T.MEMBER_ID
order by
R.REVIEW_DATE, R.REVIEW_TEXT;