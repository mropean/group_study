import sys
N = sys.stdin.readline()
list_ = [0] * 10001

for _ in range(int(N)):
    list_[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(0, list_[i]):
        print(i)
