from collections import deque # bfs용
import sys

# dfs
def dfs(start):
    global cnt
    V[start] = cnt # 해당 점에 몇 번째로 방문했는지
    # 24479, 24480 번
    E[start].sort(reverse = False) # 점과 연결된 접점들 정렬(오름차순 방문)
    # E[start].sort(reverse = True) # 점과 연결된 접점들 정렬(내림차순 방문)

    for i in E[start]:
        if not V[i]: # 방문한적 없는 점이면
            cnt += 1
            dfs_v.append(i)
            dfs(i) # 해당 점으로 이동
# bfs
def bfs(start):
    global cnt

    q = deque([r])
    V[r] = 1
    while q:        
        start = q.popleft()

        # 연결된 자표들 중에서
        for e in E[start]:
            # 방문한적 없는 점이라면
            if V[e] == 0:
                cnt += 1
                # N 번째 방문했다.
                V[e] = cnt
                bfs_v.append(e)
                q.append(e)

# 정점수,간선수, 시작지점
n,m,r = map(int, input().split())

# 접점 - 접점(간선) 리스트
E = [[] for _ in range(n+1)]

# 방문순서
dfs_v = []
bfs_v = []

for _ in range(m):
    u, v = map(int, input().split())
    # ex 1 4 입력시
    # 리스트 1번 인덱스에 4 추가
    # 리스트 4번 인덱스에 1 추가
    E[u].append(v) # 해당 정점과 연결된 정점 추가
    E[v].append(u) # 연결된 점정에 해당 정점 추가

cnt = 1
V = [0]*(n+1)
dfs_v.append(r)
dfs(r)

cnt = 1
V = [0]*(n+1)
bfs_v.append(r)
bfs(r)

print(*dfs_v)
print(*bfs_v)
