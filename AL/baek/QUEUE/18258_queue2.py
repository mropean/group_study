from collections import deque
import sys

T = int(sys.stdin.readline())
d = deque()

for _ in range(T):
    # 시간 복잡도 1
    # 입력1 : 1행동
    in_ = sys.stdin.readline().split()
    if in_[0] == "push":
        d.append(in_[1])
        
    elif in_[0] == "pop":
        try:
            print(d.popleft())
        except:
            print(-1)
            
    elif in_[0] == "front":
        if len(d):
            print(d[0])
        else:
            print(-1)
            
    elif in_[0] == "back":
        if len(d):
            print(d[-1])
        else:
            print(-1)
            
    elif in_[0] == "empty":
        if len(d):
            print(0)
        else:
            print(1)
            
    elif in_[0] == "size":
        print(len(d))
        
