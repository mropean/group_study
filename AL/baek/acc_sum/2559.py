import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
num_list = list(map(int, input().split()))

sum_list = []
sum_list.append(sum(num_list[:K]))
                  
for i in range(N - K):
    sum_list.append(sum_list[i] - num_list[i] + num_list[i+K])

print(max(sum_list))
