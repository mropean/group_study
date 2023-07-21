from sys import stdin
N, M = list(map(int, stdin.readline().split()))
temp = []

def back1(_list, n, m):
    if len(_list) == m:
        print(*_list)
        return
    else:
        num = max(_list) if len(_list) > 1 else 0
        for i in range(num+1, n+1):
            if len(_list) >= 1 and max(_list) >= i:
                continue
            _list.append(i)
            back1(_list, n, m)
            _list.pop()

back1(temp, N, M)