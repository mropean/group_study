import sys
N, M = list(map(int, sys.stdin.readline().split()))
no_L = set(sys.stdin.readline().strip() for i in range(N))
no_S = set(sys.stdin.readline().strip() for i in range(M))
no_LS = no_L & no_S
print(len(no_LS))
for i in sorted(list(no_LS)):
    print(i)
