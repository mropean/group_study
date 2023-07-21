import sys
N = int(sys.stdin.readline())
flag = 0
for i in range(N):
    if (i + sum(list(map(int,(" ".join(str(i)).split()))))) == N:
        print(i)
        flag = 1
        break
if flag == 0:
    print(0)
