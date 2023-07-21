import itertools
import sys
N, M = list(map(int, sys.stdin.readline().split()))

arr = [i for i in range(1, N+1)]
nPr = itertools.combinations(arr, M)
for i in list(nPr):
    print(*i)