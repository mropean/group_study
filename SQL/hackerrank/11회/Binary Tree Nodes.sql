select
N,
CASE
    WHEN P IS NULL THEN "Root"
    WHEN N IN (select P from BST) THEN "Inner"
    ELSE "Leaf"
END
from
BST
order by
N