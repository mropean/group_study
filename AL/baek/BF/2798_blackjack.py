import sys
N, w = map(int, (sys.stdin.readline()).split())
list_ = sorted(list(map(int, (sys.stdin.readline()).split())))
# 한번 정렬

max_ = 0
flag = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = list_[i] + list_[j] + list_[k]
            if max_ == 0:
                max_ = temp
            else:
                if w == temp:
                    print(temp)
                    flag = 1
                elif max_ < temp:
                    # 정렬했으므로
                    # 원하는 값보다 클경우 뒤는 안봐도 됨
                    if temp < w:
                        max_ = temp
                    else:
                        break

        if flag != 0:
            break
        
    if flag != 0:
        break

if flag == 0:
    print(max_)
