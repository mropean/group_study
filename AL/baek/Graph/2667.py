import sys
input = sys.stdin.readline

N = int(input())
n_map = [ list(map(int, " ".join(input()).split())) for _ in range(N) ]
g_cnt = 0
cnt = 0
result = []

# r,c 일때의 조합 -> 0,1 / 0,-1 / 1,0 / -1,0
# 즉, 상하좌우를 확인한다.
rows = [0, 0, 1, -1]
cols = [1, -1, 0, 0]


def dfs(r, c):
    global cnt
    # 해당 좌표값이 N의 범위를 넘어가거나 배열의 시작점을 넘어간경우
    if r < 0 or r >= N or c < 0 or c >= N:
        return False

    # 해당좌표값이 1인경우 (존재)
    if n_map[r][c] == 1:
        # 해당 단지 갯수 + 1
        cnt += 1
        # 해당 좌표 0으로 변경
        n_map[r][c] = 0
        # 4개 범위(상하좌우)위치로 이동
        for i in range(4):
            nr = r + rows[i]
            nc = c + cols[i]
            dfs(nr, nc)
        return True    
    return False

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result.append(cnt)
            g_cnt += 1
            cnt = 0

# 단지내 집의 수 오름차순 정렬
result.sort()
print(g_cnt)
for i in result:
    print(i)
