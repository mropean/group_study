-- 코드를 입력하세요
SELECT
A.AUTHOR_ID, AUTHOR_NAME, CATEGORY, TOTAL_SALES
from
AUTHOR A
    join
    (
        select
        CATEGORY, AUTHOR_ID, SUM(PRICE * SALES) as TOTAL_SALES
        from
        BOOK B
            join
            (
                select
                book_id, SUM(SALES) as SALES
                from
                BOOK_SALES
                where
                YEAR(SALES_DATE) = 2022
                and
                MONTH(SALES_DATE) = 1
                group by
                book_id
            ) as S
            on
            B.BOOK_ID = S.BOOK_ID
        group by
        AUTHOR_ID, CATEGORY
    ) as B
    on
    A.AUTHOR_ID = B.AUTHOR_ID
order by
A.AUTHOR_ID, CATEGORY desc
;