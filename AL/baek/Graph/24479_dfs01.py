# 오름차순: https://aigong.tistory.com/469
import sys
sys.setrecursionlimit(10**9) # 재귀를 이용할경우, 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def dfs(start):
    global cnt
    V[start] = cnt # 해당 점에 몇 번째로 방문했는지
    # 24479, 24480 번
    E[start].sort(reverse = False) # 점과 연결된 접점들 정렬(오름차순 방문)
    # E[start].sort(reverse = True) # 점과 연결된 접점들 정렬(내림차순 방문)

    for i in E[start]:
        if not V[i]: # 방문한적 없는 점이면
            cnt += 1
            dfs(i) # 해당 점으로 이동

# 정점수,간선수, 시작지점
n,m,r = map(int, input().split())

# 접점 - 접점(간선) 리스트
E = [[] for _ in range(n+1)]

# 방문지점
V = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    # ex 1 4 입력시
    # 리스트 1번 인덱스에 4 추가
    # 리스트 4번 인덱스에 1 추가
    E[u].append(v) # 해당 정점과 연결된 정점 추가
    E[v].append(u) # 연결된 점정에 해당 정점 추가

cnt = 1
dfs(r)
for i in V[1:]:
    print(i)
