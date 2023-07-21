import sys
def w(a, b, c):
    # 조건 1
    if a<=0 or b<=0 or c<=0:
        return 1
    # 조건 2
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    # 이미 저장되어있는 값이면 (이전에 저장된 값이 있으면)
    # 왜? -> 임의의 a,b,c, 이전에 불른 a,b,c여도 각 위치의 값들은 동일하기 때문이다
    # 예를들어 20, 20, 20이 불러와졌을 때, 9, 9, 9 를 지나쳐간다 해보자.
    # 내가 9, 9, 9 를 넣었을 때도 리스트[9][9][9] 값은 동일할 것이다.
    elif _list[a][b][c]:
        return _list[a][b][c]
    # 조건 3
    elif a<b<c:
        _list[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return _list[a][b][c]
    # 조건 4
    else:
        _list[a][b][c] = w(a-1,b,c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return _list[a][b][c]

_list = [[[0] * 21 for _ in range(21)] for _ in range(21)]
while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")    