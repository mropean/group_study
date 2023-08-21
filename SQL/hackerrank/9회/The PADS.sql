select
CONCAT(Name, "(", 
       CASE
            WHEN (Occupation = "Professor") THEN "P"
            WHEN (Occupation = "Actor") THEN "A"
            WHEN (Occupation = "Doctor") THEN "D"
            WHEN (Occupation = "Singer") THEN "S"
       END, 
       ")") as info
from
OCCUPATIONS
order by
info;
select
CONCAT("There are a total of ", COUNT(*),
      CASE
            WHEN (Occupation = "Professor") THEN " professors."
            WHEN (Occupation = "Actor") THEN " actors."
            WHEN (Occupation = "Doctor") THEN " doctors."
            WHEN (Occupation = "Singer") THEN " singers."
      END)
from
OCCUPATIONS
group by
Occupation
order by
COUNT(*), Occupation;