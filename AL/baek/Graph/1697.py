from collections import deque
import sys
input = sys.stdin.readline
n, k = list(map(int, input().split()))

# 규칙 3가지
rule = [lambda x : x+1 , lambda x : x-1, lambda x : x*2]
# 해당 인덱스(값에) 몇번 째(level)에 도착했는지
d = [0] * ((10 ** 5) + 1)
# bfs용 덱
q = deque()

def bfs(num):
    # 수빈이 위치
    q.append(num)

    while q:
        #print(q)
        #print(d[:100])
        num = q.popleft()
        if num == k:
            print(d[num])
            
            break

        for i in range(3):
            nx = rule[i](num)
            #print("num:", num, "nx:", nx)
            # 범위값안쪽, 도달하지 못한 위치인경우
            # 만약 도달했다면?
            # 그곳이 답이라면 멈췄을 것이고,
            # 거치는 곳이면 덱에 다음 레벨의 값들이 이미 들어가있다.
            if 0 <= nx <= 10**5 and not d[nx]:
                # 현재 위치의 레벨값에 + 1을 더해
                # 다음 레벨에 도착했다 설명
                d[nx] = d[num] + 1
                q.append(nx)

bfs(n)
            

            
