from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

r = 1

E = [[] for _ in range(n + 1)] # 0 1 2 3 4 5 6
V = [0] * (n + 1) # 0 1 2 3 4 5 6

cnt = 1

# [ 0X
#  1 -> [ , ,]
# ]

for _ in range(m):
    u, v = map(int, input().split())
    # ex 1 4 입력시
    # 리스트 1번 인덱스에 4 추가
    # 리스트 4번 인덱스에 1 추가
    E[u].append(v) # 해당 정점과 연결된 정점 추가
    E[v].append(u) # 연결된 점정에 해당 정점 추가

def bfs(start):
    global cnt

    q = deque([r])
    V[r] = 1

    while q:

        start = q.popleft()

        # 현재 좌표와 연결된 점들
        E[start].sort(reverse=False) # 오름차순으로 정렬

        # 연결된 자표들 중에서
        for e in E[start]:
            # 방문한적 없는 점이라면

            if V[e] == 0:
                cnt += 1
                # N 번째 방문했다.
                V[e] = cnt
                q.append(e)
bfs(r)

print(cnt-1)
