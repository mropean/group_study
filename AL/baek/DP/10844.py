import sys
input = sys.stdin.readline

N = int(input())
dp = [ [0] * 10 for _ in range(N + 1) ]

# 1층 값
dp[1] = [0,1,1,1,1,1,1,1,1,1] # 1자리수, 0을 제외한 모든 수가 계단 

# 2층 부터
# dp[i] -> 자리수 i
# dp[i][j] -> 마지막 자리가 j
for i in range(2, N+1):
    for j in range(10):
        # 앞의 수가 0일 경우 뒤에 올 수 있는 값은 1 하나
        if (j == 0):
            dp[i][j] = dp[i-1][1]
        # 앞의 수가 1~8의 값을 가질 때, 2개의 수를 가진다.
        elif (1 <= j <= 8):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        # 앞의 수가 9일 경우 뒤에 올 수 있는 값은 8 하나
        else:
            dp[i][j] = dp[i-1][8]
    print(dp[i])

print(sum(dp[N]) % 1000000000)
