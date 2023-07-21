import sys
input = sys.stdin.readline

X = int(input())
dp = [0] * (X+1)

for i in range(2, X+1):
    # 1을 뺏을때, 1 이전의 위치(인덱스) 값에서 +1 (현재값)
    dp[i] = dp[i-1]+1

    # 현재 인덱스에서
    
    # 2로 나누어질때, 몫의 위치(인덱스) 값 + 1과 현재 값중 최소값
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

    # 3도 마찬가지
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

    ## 즉 현재 위치(인덱스) 값까지 최소로 올 수 있는 값을 찾는다.

print(dp[-1])
