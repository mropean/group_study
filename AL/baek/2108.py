import sys
from collections import Counter

N = int(sys.stdin.readline())
list_ = [int(sys.stdin.readline()) for i in range(int(N))]

list_ = sorted(list_)

# 산술평균
print(round(sum(list_) / N))

# 중앙값
print(list_[int(N / 2)])

# 최빈값
## list 반환
## list의 각 원소는 tuple
## (리스트 원소, 갯수)형태
count = Counter(list_).most_common(2)
if len(count) > 1:
    if count[0][1] > count[1][1]:
        print(count[0][0])
    else:
        print(count[1][0])
else:
    print(count[0][0])
    
# 범위
print(list_[-1] - list_[0])
