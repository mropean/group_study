select
c.company_code, founder, 
COUNT(DISTINCT lm.lead_manager_code), 
COUNT(DISTINCT sm.senior_manager_code), 
COUNT(DISTINCT m.manager_code), 
COUNT(DISTINCT e.employee_code)
from
Company c
    join
        Lead_Manager as lm
    on
        c.company_code = lm.company_code
    join
        Senior_Manager as sm
    on
        c.company_code = sm.company_code
    join
        Manager as m
    on 
        c.company_code = m.company_code
    join
        Employee as e
    on
        c.company_code = e.company_code
group by
c.company_code, founder