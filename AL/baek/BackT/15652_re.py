from sys import stdin
N, M = list(map(int, stdin.readline().split()))
temp = []

def back3(_list, n, m):
    if len(_list) == m:
        print(*_list)
        return
    else:
        for i in range(1, n+1):
            if len(_list) >= 1 and max(_list) > i:
                continue
            _list.append(i)
            back3(_list, n, m)
            _list.pop()

back3(temp, N, M)