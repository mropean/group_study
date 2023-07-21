import sys
from collections import deque
inp = sys.stdin.readline
N, M = list(map(int, inp().split()))
w_list = list(map(int, inp().split()))
count = 0

d = deque([ i+1 for i in range(N) ])
for i in w_list: # [7]
    
    while True:
        # 원하는 수라면 첫번째원소 pop
        if i == d[0]:
            d.popleft()
            break
        # 원하는 수가 덱의 몇번째 인덱스에 있나?
        
        index = d.index(i)

        ## 위 인덱스를 기준으로 왼쪽값이 오른쪽값보다 작으면 왼쪽으로 회전
        ## 아니라면 오른쪽으로 회전
        ## 둘이같으면 왼쪽으로 회전에서 찾기.
        ## (왜? (왼쪽 + 오른쪽) 회전한 수 이기 때문에)

        # R
        if (len(d)-1) - index <= index - 1:
            d.appendleft(d.pop())
            count += 1
        # L
        else:
            d.append(d.popleft())
            count += 1

print(count)
