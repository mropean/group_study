from collections import deque
import sys
N = int(sys.stdin.readline())

# 1부터 N까지의 숫자 리스트
d = deque([i+1 for i in range(N)])

flag = True
# 1개 남을때 까지.
while len(d) != 1:
    # 앞 카드 버리고
    if flag:
        d.popleft()
        flag = False
    # 뒷 카드 제일 아래(뒤)로 옮기
    else:
        d.append(d.popleft())
        flag = True

print(d.popleft())
