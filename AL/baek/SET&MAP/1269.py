import sys
_ = sys.stdin.readline()
list_a = set(map(int, sys.stdin.readline().split()))
list_b = set(map(int, sys.stdin.readline().split()))

print(len(list_a - list_b) + len(list_b - list_a))
