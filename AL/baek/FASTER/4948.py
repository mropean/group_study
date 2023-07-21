from collections import Counter
import math
import sys
in_F = sys.stdin.readline

def Prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

# 입력값은 123456 이하이다.
# 베르트랑 공준은 임이의 자연수 n에 대해, n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.
# list_p는 123456 * 2 배 크기로 미리 할당해 둔다.
list_p = [0] * ((123456 * 2) + 1)
# 할당된 리스트의 인덱스를 통해 미리 소수를 판별한다.
for i in range(1, ((123456 * 2) + 1)):
    if Prime(i):
        # 해당 인덱스가 소수라면 (list_p[2] == 2)
        # 1을 저장해둔다.
        list_p[i] = 1
       
while True:
    i = int(in_F())
    if i == 0:
        break
    # Counter를 사용해 집계한다.
    # list_p는 두개의 값(0, 1)이다.
    # Counter로 반환된 딕셔너리는 
    # {0: "0의 갯수", 1: "1의 갯수"} 와 같은 형태이다.
    # "n보다 크고 2n보다 작거나 같은" = n+1 ~ 2n 까지의 범위
    # list_p의 해당 범위안에서 집계한다.
    list_P = Counter(list_p[i+1:i*2+1])
    print(list_P[1])

