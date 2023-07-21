import sys
N = int(sys.stdin.readline())
list_ = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
temp = []

for i in range(len(list_)):
    count = 1
    for j in range(len(list_)):
        if i == j:
            continue
        else:
            if list_[i][0] < list_[j][0]:
                if list_[i][1] < list_[j][1]:
                    count += 1
    temp.append(count)

print(" ".join(str(s) for s in temp))
