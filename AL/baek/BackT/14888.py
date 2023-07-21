# 브루트포스
# https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
import sys
input = sys.stdin.readline

def dfs(depth, res, pl, mi, mu, di):
    global n, min_, max_
    if depth == n:
        max_ = max(res, max_)
        min_ = min(res, min_)
        print("max:", max_, "min:", min_)
        return

    # 각 연산자가 0이 아닐때까지
    if pl: # 2111 / 1111/ 0111/ 0011/ 0001 / 0010
        print(f"depth = {depth} 더하기 재귀 시작 +-*/ = ", pl-1, mi, mu, di)
        dfs(depth+1, res + num_list[depth], pl-1, mi, mu, di)
        print(f"depth = {depth} 더하기 재귀 끝")
    if mi:
        print(f"depth = {depth} 빼기 재귀 시작 +-*/ = ", pl, mi-1, mu, di)
        dfs(depth+1, res - num_list[depth], pl, mi-1, mu, di)
        print(f"depth = {depth} 빼기 재귀 끝")
    if mu:
        print(f"depth = {depth} 곱하기 재귀 시작 +-*/ = ", pl, mi, mu-1, di)
        dfs(depth+1, res * num_list[depth], pl, mi, mu-1, di)
        print(f"depth = {depth} 곱하기 재귀 끝")
    if di:
        print(f"depth = {depth} 나누기 재귀 시작 +-*/ = ", pl, mi, mu, di-1)
        dfs(depth+1, int(res / num_list[depth]), pl, mi, mu, di-1)
        print(f"depth = {depth} 나누기 재귀 끝")

n = int(input())
num_list = list(map(int, input().split()))
oper = list(map(int, input().split())) # + - * //

min_ = float('inf') # 최대값
max_ = float('-inf') # 최소값
dfs(1, num_list[0], oper[0], oper[1], oper[2], oper[3])

print(max_)
print(min_)
