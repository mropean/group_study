select
hsc.hacker_id, hsc.name
from
Difficulty d
    join
    (
        select
        hs.hacker_id, hs.name, hs.score, c.difficulty_level
        from
        Challenges c
            join
            (
                select
                h.hacker_id, name, challenge_id, score 
                from
                Hackers h
                    join
                    Submissions as s
                    on
                    h.hacker_id = s.hacker_id
            ) as hs
            on
            c.challenge_id = hs.challenge_id
    ) as hsc
    on
    d.difficulty_level = hsc.difficulty_level
where
hsc.score = d.score
group by
hsc.hacker_id, hsc.name
having
COUNT(*) > 1
order by
COUNT(*) desc, hsc.hacker_id 