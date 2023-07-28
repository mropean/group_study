-- 코드를 입력하세요
SELECT
CATEGORY, SUM(SALES)
from
BOOK_SALES
    inner join
    BOOK
    on
    BOOK_SALES.BOOK_ID = BOOK.BOOK_ID
where
YEAR(SALES_DATE) = 2022
and
MONTH(SALES_DATE) = 1
group by
CATEGORY
having
SUM(SALES)
order by
CATEGORY;