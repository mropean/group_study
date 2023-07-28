import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
num_list = list(map(int, input().split()))

sum_list = []
# k 갯수 초기값 저장
sum_list.append(sum(num_list[:K]))

print(sum_list)
for i in range(N - K):
    print(sum_list[i], num_list[i], num_list[i+K])
    # sum_list[i]는 k 갯수만큼 저장된 값
    # num_list[i]는 sum_list[i]에 처음 더해진 값
    # num_list[i+k]는 다음으로 더해져야 할 값

    ## 예를들면
    # k = 3 일때,
    # num_list 가 a, b, c, d, e, f가 있다고 가정하면
    # 현재 더해진 값은 (a+b+c) 라고 할때,
    # 다음으로 누적되어 더해저야 할 값은
    # 현재 값(a+b+c)에서 a가 빠지고 d가 저장되어야 한다.
    
    sum_list.append(sum_list[i] - num_list[i] + num_list[i+K])
    print(sum_list)

print(max(sum_list))
