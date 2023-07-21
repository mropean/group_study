import itertools
import sys
N, M = list(map(int, sys.stdin.readline().split()))

arr = [range(1, N+1) for _ in range(M)]
nPr = itertools.product(*arr)
for i in list(nPr):
    print(*i)