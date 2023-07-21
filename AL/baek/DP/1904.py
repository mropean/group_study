n = int(input())
# DP
def fibonacci(n):
    f[0] = 1
    f[1] = 2
    for i in range(2, n):
        f[i] = (f[i - 1] + f[i - 2]) % 15746
    
    return f[n-1]


f = [0] * (n)
if n != 1:
    res = fibonacci(n)
    print(res)
else:
    print(1)