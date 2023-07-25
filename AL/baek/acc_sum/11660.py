# https://sodehdt-ldkt.tistory.com/76
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [ list(map(int, input().split())) for _ in range(n) ]

temp_list = [ [0] * (n+1) for _ in range(n+1) ]
for i in range(1, n+1):
    for j in range(1, n+1):
        temp_list[i][j] = temp_list[i][j-1] + temp_list[i-1][j] - temp_list[i-1][j-1]  + num_list[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = temp_list[x2][y2] - temp_list[x2][y1-1] - temp_list[x1-1][y2] + temp_list[x1-1][y1-1]
    print(res)
