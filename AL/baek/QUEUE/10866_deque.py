import sys
inp = sys.stdin.readline
N = int(inp())
cmd = [ inp().split() for i in range(N) ]

deq = []
for c in cmd:
    if c[0] == "push_front":
        deq.insert(0, c[1])
    elif c[0] == "push_back":
        deq.append(c[1])
    elif c[0] == "pop_front":
        try:
            print(deq[0])
            del deq[0]
        except:
            print(-1)
    elif c[0] == "pop_back":
        try:
            print(deq.pop())
        except:
            print(-1)
    elif c[0] == "size":
        print(len(deq))
    elif c[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == "front":
        try:
            print(deq[0])
        except:
            print(-1)
    elif c[0] == "back":
        try:
            print(deq[-1])
        except:
            print(-1)
