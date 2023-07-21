import sys
input = sys.stdin.readline

def row(n, x):
    for i in range(9):
        # 이미 있는 숫자라면
        if sudoku[x][i] == n:
            return False
    # 해당하지 않는 숫자라면
    return True

def col(n, y):
    for i in range(9):
        # 이미 있는 숫자라면
        if sudoku[i][y] == n:
            return False
    # 해당하지 않는 숫자라면
    return True

def rect(x, y, n):
    x = x//3 * 3
    y = y//3 * 3

    # 사각형의 크기 3*3
    for i in range(3):
        for j in range(3):
            # 이미 있는 숫자라면
            if sudoku[x+i][y+j] == n:
                return False
    # 해당하지 않는 숫자라면
    return True

def dfs(num):
    # 채운수가 좌표의 갯수와 같으면
    if num == len(z_list):
        for i in range(9):
            print(*sudoku[i])
        # 종료
        exit(0)

    # 채울 숫자는 1~9
    # z_list 비어있는 좌표의
    # num = len(z_list)
    for i in range(1, 10):
        # 비어있는 곳
        x = z_list[num][0]
        y = z_list[num][1]

        # 행 - 열 - 사각형의 조건이 맞는지 확인
        # 숫자 i 가 행, 열, 사각형에 없으면
        if row(i, x)and col(i, y) and rect(x, y, i):
            # 해당 빈칸은 i값을 가진다.
            sudoku[x][y] = i
            dfs(num + 1)
            # 재귀를 탈출했으면 다른 숫자일 확률이 더 크다.
            sudoku[x][y] = 0

# 스도쿠
sudoku = []
# 비어있는 좌표
z_list = []
for i in range(9):
    sudoku.append(list(map(int, input().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
          z_list.append([i, j])

# 파라미터 값은 비워있는 곳을 채운 수
dfs(0)
