import sys
N = int(sys.stdin.readline())

list_ = []
for i in range(N):
    a, b = sys.stdin.readline().strip().split(" ")
    list_.append([int(a), i, b])

list_ = sorted(list_)

for i in list_:
    print(i[0], i[2])
