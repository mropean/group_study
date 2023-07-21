import sys
N, M = list(map(int, sys.stdin.readline().split()))
S = [sys.stdin.readline().strip() for i in range(N)]
list_ = [sys.stdin.readline().strip() for i in range(M)]

count = 0
for i in list_:
    if i in S:
        count += 1

print(count)
