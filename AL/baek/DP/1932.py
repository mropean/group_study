import sys
N = int(sys.stdin.readline())
_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(_list[i])):
        # 현재 계층의 맨 왼쪽값이면
        if j == 0:
            # 이전 계층의 맨 왼쪽값 더하기
            _list[i][j] += _list[i-1][j]
        # 현재 계층의 마지막 값이면
        elif j == len(_list[i]) - 1:
            # 이전 계층의 맨 오른쪽(마지막)값 더하기
            _list[i][j] += _list[i-1][j-1]
        # 현재 계층의 중간에 위치한 값이면
        else:
            # 이전 계층의 왼쪽, 오른쪽중에서 최대값으로 더하기
            # 현재 계층 (_list[i][j])
            # 이전 계층의 왼쪽 (_list[i-1][j-1])
            # 이전 계층의 오른쪽 (_list[i-1][j])
            _list[i][j] = max(_list[i][j] + _list[i-1][j-1], _list[i][j] + _list[i-1][j])

# 마지막 계층에서 최대값 찾기            
print(max(_list[N-1]))
