select
months * salary as cost, COUNT(*)
from
Employee
group by
cost
order by
cost desc
limit 1;