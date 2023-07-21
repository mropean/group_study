import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))

t_list = [0]
t_list.extend(list(itertools.accumulate(n_list)))

for _ in range(M):
    s, e = map(int, input().split())
    print(t_list[e] - t_list[s-1])
    
