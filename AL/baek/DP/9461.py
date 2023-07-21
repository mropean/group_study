import sys
T = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(T)]

_list = [0] * max(N)
for i in range(len(_list)):
    if i < 3:
        _list[i] = 1
    elif i < 5:
        _list[i] = 2
    else:
        _list[i] = _list[i-3] + _list[i-4] + _list[i-5]

for i in N:
    print(_list[i-1])
