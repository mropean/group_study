-- 코드를 입력하세요
SELECT
info.REST_ID, info.REST_NAME, info.FOOD_TYPE, info.FAVORITES, info.ADDRESS, review.REVIEW_SCORE
from
REST_INFO info
    inner join
        (
            select
            REST_ID, ROUND(AVG(REVIEW_SCORE), 2) as REVIEW_SCORE
            from
            REST_REVIEW
            group by
            REST_ID
        ) as review
    on
    info.REST_ID = review.REST_ID
where
ADDRESS
LIKE "서울%"
order by
REVIEW_SCORE desc, FAVORITES desc
;