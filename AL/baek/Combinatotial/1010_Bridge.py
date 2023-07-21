import sys, math
T = int(sys.stdin.readline())
list_ = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]
for i in list_:
    print(math.factorial(i[1]) // (math.factorial(i[0]) * math.factorial(i[1] - i[0])))
