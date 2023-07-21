import sys
N, M = list(map(int, sys.stdin.readline().split()))
dic_ = {sys.stdin.readline().strip():i+1 for i in range(N)}
list_ = list(dic_.keys())

for i in range(M):
    in_ = sys.stdin.readline().strip()
    if in_ < "A":
        print(list_[int(in_)-1])
    else:
        print(dic_[in_])
