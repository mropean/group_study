from collections import deque
import sys
input = sys.stdin.readline
m, n = list(map(int, input().split()))
mn_map = [ list(map(int, " ".join(input()).split())) for _ in range(m) ]

# r,c 일때의 조합 -> 0,1 / 0,-1 / 1,0 / -1,0
# 즉, 상하좌우를 확인한다.
rows = [0, 0, 1, -1]
cols = [1, -1, 0, 0]

# bfs용 덱
q = deque()

def bfs(c, r):

    q.append((c, r))

    while q:
        c, r = q.popleft()
        # 4개 범위(상하좌우)위치의 좌표들 덱에 넣기
        for i in range(4):
            nc = c + cols[i]
            nr = r + rows[i]
            
            # 해당 좌표값이 N의 범위를 넘어가거나 배열의 시작점을 넘어간경우
            if nc < 0 or nc >= m or nr < 0 or nr >= n:
                continue
            # 지도의 값이 벽(0) 이 아닐경우
            if mn_map[nc][nr] == 1:
                # 해당 1의 값은 이전값(몇번째 칸인지)에 1을 더하게 된다.
                mn_map[nc][nr] = mn_map[c][r] + 1
                #print(mn_map)
                q.append((nc, nr))

    return mn_map[m-1][n-1]
                


print(bfs(0, 0))
