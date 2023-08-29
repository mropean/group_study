with occ as(
    select Occupation, Name, RANK() OVER (
        partition by
        Occupation
        order by
        Name
    ) as occ_name
    from
    OCCUPATIONS
)

select
    MIN(CASE
            WHEN Occupation = "Doctor" THEN Name
        ELSE null
        END),
    MIN(CASE
            WHEN Occupation = "Professor" THEN Name
        ELSE null
        END),
    MIN(CASE
            WHEN Occupation = "Singer" THEN Name
        ELSE null
        END),
    MIN(CASE
            WHEN Occupation = "Actor" THEN Name
        ELSE null
        END)
from
occ
group by
occ_name