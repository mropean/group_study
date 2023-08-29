select
IF(g.GRADE > 7, s.Name, "NULL"), g.GRADE, s.Marks
from
STUDENTS s
    left join
        GRADES g
        on
        s.Marks BETWEEN g.MIN_MARK and g.MAX_MARK
order by
g.GRADE DESC, s.NAME