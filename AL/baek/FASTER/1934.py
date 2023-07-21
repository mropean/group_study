import sys
N = int(sys.stdin.readline())
# N = int(input())

def DoubleDiv(x, y):
    temp = []
    num = 2

    while True:
        if (x < num) or (y < num):
            break
        else:
            if (x % num == 0) and (y % num == 0):
                temp.append(num)
                x = x // num
                y = y // num
                
            else:
                num += 1
    temp.extend([x, y])
    return temp

for i in range(N):
    temp = []
    # x, y = list(map(int, (input().split())))
    x, y = list(map(int, sys.stdin.readline().split()))
    
    if x < 2 or y < 2:
        temp = [x * y]
    else:
        temp = DoubleDiv(x, y)
    print(eval("*".join(map(str, temp))))        
