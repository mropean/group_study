import sys
import math
x1, y1 = list(map(int, sys.stdin.readline().split()))
x2, y2 = list(map(int, sys.stdin.readline().split()))
y = math.lcm(y1, y2) # y는 두 분모의 최소공배수
x = ((y // y1) * x1) + ((y // y2) * x2) # 분수의 분자값 구하는 식
gcd_ = math.gcd(x, y) # x,y의 최대공약수 = gcd
print(x // gcd_, y // gcd_) # 두수를 최대 공약수로 나눠 주면 기약분수
