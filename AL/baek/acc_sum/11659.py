import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))

t_list = [0]
## itertools.accumulate(숫자 리스트)
# 0번 인덱스부터 마지막 인덱스까지 누적해서 더해간다.
t_list.extend(list(itertools.accumulate(n_list)))

for _ in range(M):
    s, e = map(int, input().split())
    print(t_list[e] - t_list[s-1])
    
