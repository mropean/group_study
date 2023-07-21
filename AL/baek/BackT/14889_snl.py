# https://aigong.tistory.com/478
# 브루트포스 알고리즘 사용
from sys import stdin
input = stdin.readline

# 재귀로 구현
def dfs(depth, idx):
    global n, res

    # 입력된 인원(짝)수의 절반까지 한팀
    if depth == n//2:
        p1, p2 = 0, 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # 현재 팀에 소속된 인원(True)
                elif v[i] and v[j]:
                    p1 += sij[i][j]
                    print("+p1",p1," i+1",i+1," j+1", j+1," sij::", sij[i][j])
                # 소속되지 않은 인원(False)은 다른팀
                elif not v[i] and not v[j]:
                    p2 += sij[i][j]
                    print("@p2",p2," i+1",i+1," j+1", j+1," sij::", sij[i][j])
        # 최소값 찾기
        res = min(res, abs(p1-p2))
        print()
        return

    # 절반이 안되면
    # 방문한적 없는 인원 팀에 넣기
    # false인 인원은 다른팀
    for i in range(idx, n):
        if not v[i]:
            v[i] = True
            print(i+1, "인원 재귀시작")
            dfs(depth+1, i+1)
            print(i+1, "인원 재귀 끝")
            v[i] = False


n = int(input())
sij = [list(map(int, input().split())) for _ in range(n) ]
v = [False for _ in range(n)] # 해당 인원을 방문했는지
res = 200 # 최소값 abs((1+1) - (100+100)) 198

dfs(0, 0)
print(res)
