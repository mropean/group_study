import sys
M, N = list(map(int, sys.stdin.readline().split()))
list_ = [sys.stdin.readline().strip() for i in range(M)]

answer = -1
for i in range(M-7):
    for j in range(N-7):
        min_w = 0
        min_b = 0
        flag = 0        
        for m in range(i, i+8):
            for n in range(j, j+8):
                if flag == 0:
                    if list_[m][n] == "B":
                        min_w += 1
                    else:
                        min_b += 1

                    flag = 1
                else:
                    if list_[m][n] == "W":
                        min_w += 1
                    else:
                        min_b += 1

                    flag = 0
                    
            flag = 0 if flag == 1 else 1
            
        if answer == -1:
            answer = min_w if min_w <= min_b else min_b
        else:
            if min_w <= min_b:
                if answer >= min_w:
                    answer = min_w
            else:
                if answer >= min_b:
                    answer = min_b

print(answer)  
