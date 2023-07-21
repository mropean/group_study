import math
import sys
in_F = sys.stdin.readline

# 일반적인 소수 찾는 함수
# 들어온 값이 소수인지 찾는다
def Prime(num):
    # 2 미만 (0, 1)은 아니다
    if num < 2:
        return False
    # 2부터 루트(입력된값) 까지만 찾는다
    # 이유가 궁금하면 https://namu.wiki/w/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%20%EC%B2%B4#toc (킹무위키: 에라토스테네스의 체) 참고
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


N, M = list(map(int, (in_F().split())))
# 입력된 값 사이의 소수만 출력한다.
for i in range(N, M+1):
    if Prime(i):
        print(i)