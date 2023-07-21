from sys import stdin
N = int(stdin.readline())

temp = [0] * N
count = 0

def check(n):
    for i in range(n):
        if temp[n] == temp[i] or abs(temp[n] - temp[i]) == n-i:
            return False
        
    return True
                
def queen(n):
    global count
    if n == N:
        print(temp)
        count += 1
        return
    else:
        for i in range(N):
            temp[n] = i

            if check(n):
                queen(n+1)
        
queen(0)
print(count)
