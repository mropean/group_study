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
#print(acc) 3 2 0

res = acc[0]
# 3 + 3C2 + 2C2 + 0C0 = 7
for i in acc:
    res += i*(i-1)//2 # 조합(Combination)식 i_C_2
        
print(res)
        
                    
