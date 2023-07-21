import sys
N = int(sys.stdin.readline())
data = sorted(list(set([sys.stdin.readline().strip() for i in range(N)])))
data.sort(key=len)
for i in data:
    print(i)
