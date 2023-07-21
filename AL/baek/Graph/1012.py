import sys
sys.setrecursionlimit(10**9) # 재귀를 이용할경우, 재귀 깊이 제한 늘리기
input = sys.stdin.readline

# r,c 일때의 조합 -> 0,1 / 0,-1 / 1,0 / -1,0
# 즉, 상하좌우를 확인한다.
rows = [0, 0, 1, -1]
cols = [1, -1, 0, 0]


def dfs(r, c):
    # 해당 좌표값이 N의 범위를 넘어가거나 배열의 시작점을 넘어간경우
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

    # 해당좌표값이 1인경우 (존재)

    if mn_map[r][c] == 1:
        # 해당 단지 갯수 + 1

        # 해당 좌표 0으로 변경
        mn_map[r][c] = 0
        # 4개 범위(상하좌우)위치로 이동
        for i in range(4):
            nr = r + rows[i]
            nc = c + cols[i]
            dfs(nr, nc)
        return True    
    return False

# 테스트 케이스만큼
for _ in range(int(input())):
    # 가로, 세로, 배추갯수
    m, n, k = list(map(int, input().split()))
    mn_map = [ [0]*m for i in range(n) ]
    # 위치좌표
    k_list = [ list(map(int, input().split())) for _ in range(k) ]

    # 맵에 그려두기
    for r, c in k_list:
        mn_map[c][r] = 1

    cnt = 0
    for c in range(m):
        for r in range(n):
            if dfs(r, c) == True:
                cnt += 1

    print(cnt)
