# https://smhope.tistory.com/380
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

acc = [0] * m

sum_ = 0
for i in range(n):
    sum_ += num_list[i]
    acc[sum_ % m] += 1

res = acc[0]

for i in acc:
    res += i*(i-1)//2
        
print(res)
        
                    
