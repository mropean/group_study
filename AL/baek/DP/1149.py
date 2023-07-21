import sys
input = sys.stdin.readline

N = int(input())
RGB = [ list(map(int, input().split())) for _ in range(N) ]

# 예시
# RGB[X][0] = R의 자리
# 이전 집에서 R을 제외한 G, B의 값을 확인
# 최소값을 현재 자리에 추가
for i in range(1, N):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0] # R
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1] # G
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2] # B

# 맨 마지막 RGB 리스트에서 최소값 확인
print(min(RGB[N-1]))
