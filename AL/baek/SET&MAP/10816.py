from collections import Counter
import sys
n = int(sys.stdin.readline())
counter_N = Counter(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
list_M = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    print(counter_N[list_M[i]], end="")
    if i+1 != m:
        print(" ", end="")
