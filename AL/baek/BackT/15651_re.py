from sys import stdin
N, M = list(map(int, stdin.readline().split()))
temp = []

def back2(_list, n, m):
    if len(_list) == m:
        print(*_list)
        return
    else:
        for i in range(1, n+1):
            _list.append(i)
            back2(_list, n, m)
            _list.pop()

back2(temp, N, M)