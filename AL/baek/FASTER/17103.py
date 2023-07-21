import sys
import math
in_F = sys.stdin.readline

def PrimeList(max_):
    temp = [1] * (max_+1)
    for i in range(2, int(math.sqrt(max_))+1):
        if temp[i]:
            j = 2
        while i*j <= max_:
            temp[i*j] = 0
            j += 1

    return temp

N = int(in_F())
list_ = [ int(in_F()) for _ in range(N) ]
max_num = max(list_)

list_p = PrimeList(max_num)
    
for i in list_:
    count = 0
    for j in range(2, i // 2 + 1):
        if list_p[j] and list_p[i-j]:
            count += 1
    print(count)
