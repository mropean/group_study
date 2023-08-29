select
ROUND(abs(MIN(LAT_N) - MAX(LAT_N)) + abs(MIN(LONG_W) - MAX(LONG_W)), 4)
from
STATION