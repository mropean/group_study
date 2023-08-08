-- 코드를 입력하세요
SELECT
sale.YEAR, sale.MONTH, info.GENDER, COUNT(*)
from
USER_INFO info
    left join
    (
        select
        DISTINCT YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, USER_ID
        from
        ONLINE_SALE
    ) as sale
    on
    info.USER_ID = sale.USER_ID
where
NOT sale.USER_ID IS NULL
and
NOT info.GENDER IS NULL
group by
sale.YEAR, sale.MONTH, info.GENDER
order by
sale.YEAR, sale.MONTH, info.GENDER
;