import sys
input = sys.stdin.readline

N = int(input())
s = [0] * (N + 1) # 계단 값 더할 리스트
dp = [0] * (N + 1) # 더해간 값 저장 dp 리스트

for i in range(1, N+1):
    s[i] = int(input())

# 1층이면
if N == 1:
    print(s[-1])
# 2층이면
elif N == 2:
    print(s[-2]+s[-1])
# 3층 이상이면
else:
    # 관점: 어디서 올라왔는가?
    dp[1] = s[1]
    dp[2] = s[1] + s[2]

    # 3층관점에서
    # 1+3층인가, 시작점에서 바로 2+3층인가.
    dp[3] = max(s[2] + s[3], s[1] + s[3])

    
    # 1. 직전 층에서 올라온 경우 =
    ##           s[i](지금) + s[i-1](직전) + dp[i-3](직전 밟기 전 까지의 값)
    # 2. 전전 칸에서 올라온 경우 =
    ##           s[i](지금) + dp[i-2](지금 밟기 전까지의 값)

    #### 예시)
    ### 4층
    ## 1번의 경우
    # 4층 + 3층 + (1층)
    ## 2번의 경우
    # 4층 + (2층 + 1층)
    
    ### 5층
    ## 1번의 경우
    # 5층 + 4층 + (2층 + 1층)
    ## 2번의 경우
    # 5층 + (max(3층 + 2층, 3층 + 1층))

    # 각 층의 관점에서 가질수 있는 최대값을 찾는다.
    for i in range(4, N+1):
        dp[i] = max(s[i] + s[i-1] + dp[i-3], s[i] + dp[i-2])

    print(dp[-1])
