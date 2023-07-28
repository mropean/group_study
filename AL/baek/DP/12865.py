import sys
input = sys.stdin.readline

# 물품의 수, 버틸수 있는 무게
N, K = map(int, input().split())
# 물건들의 무게와 가치
wv = [[0,0]] #
# 가방
# 물건의 무게 w = 인덱스로 사용
# 물건의 가치 v = 2차원 배열의 값
b = [ [0] * (K+1) for _ in range(N+1) ]

for _ in range(N):
    wv.append(list(map(int, input().split())))

# 물건의 갯수 만큼 각 행을 돌면서
for i in range(N+1):
    print("i=",i)
    # 가방의 크기 만큼 반복
    for j in range(1, K+1):
        print("j=", j)
        w = wv[i][0] # 무게
        v = wv[i][1] # 가치
        print("w, v = ",w,v)
        # 현재 물건이 가방크기보다 크다
        if j < w: 
            b[i][j] = b[i-1][j]
            print("b[i-1][j]=",b[i-1][j])
        else:
            print("v=", v, "b[i-1][j-w]=", b[i-1][j-w])
            print("b[i-1][j]", b[i-1][j])
            b[i][j] = max(v+b[i-1][j-w], b[i-1][j])


        print()

print(b[N][K])
