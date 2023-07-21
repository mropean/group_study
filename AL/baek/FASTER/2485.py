import math
import sys
N = int(sys.stdin.readline().strip())

pre = 0
temp = set()
in_list = set()
first = 0

for i in range(N):
    in_ = int(sys.stdin.readline().strip())
    in_list.add(in_)
    if i == 0:
        # 첫번째 값을 first, pre(이전값)에 저장
        pre = in_
        first = in_
        
    else:
        # temp에 현재 입력된 값 - 이전값 (오름차순이므로 언제나 양수)
        temp.add(in_ - pre)
        # 현재값을 pre에 저장 (t+1 시점에선 이전값이 된다)
        pre = in_

# 값들간의 차이(t시점의 가로등의 위치 - t-1시점의 가로등의 위치 = 가로등 간 사이의 길이)들의 최대공약수        
gcd_ = math.gcd(*temp)
# (마지막 가로등의 위치 - 처음 가로등의 위치) 값을 최대 공약수로 나누고 그 값을 현재 설치된 가로등의 갯수 -1 로 빼주면 새로 심어야 되는 가로수의 위치값이 된다.
print(((pre - first) // gcd_) - len(in_list) + 1)
