from itertools import combinations
import sys
N, K = list(map(int, sys.stdin.readline().split()))

print( len(list(combinations([i for i in range(N)], K))) )
# https://infinitt.tistory.com/114
# https://namu.wiki/w/%EC%9D%B4%ED%95%AD%EC%A0%95%EB%A6%AC#s-1.1
