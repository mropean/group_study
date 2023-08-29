select
Wands.id, Wands_Property.age, Wands.coins_needed, Wands.power
from
Wands
    join
    Wands_Property
    on
    Wands.code = Wands_Property.code
    join
    (
        select
        Wands_Property.age, Wands.power, MIN(Wands.coins_needed) as needed
        from
        Wands
            join
            Wands_Property
            on
            Wands.code = Wands_Property.code
        where
        Wands_Property.is_evil = 0
        group by
        Wands_Property.age, Wands.power
    ) as wwp
    on
    Wands_Property.age = wwp.age AND
    Wands.power = wwp.power AND
    Wands.coins_needed = wwp.needed
order by
Wands.power desc, Wands_Property.age desc