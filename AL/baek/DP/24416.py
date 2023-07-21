n = int(input())
# recurrence = DP 결과값
# DP
def fibonacci(n):
    global temp
    f[0] = f[1] = 1
    for i in range(2, n):
        temp += 1
        f[i] = f[i - 1] + f[i - 2]
    
    return f[n-1]

temp = 0
f = [0] * n
res = fibonacci(n)

print(res, temp)