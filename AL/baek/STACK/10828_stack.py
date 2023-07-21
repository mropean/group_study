import sys
im_stack = []
for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    # 스택에 원소 추가
    if cmd[0] == "push":
        im_stack.append(cmd[1])
    # 스택 마지막 인덱스 원소 빼기
    elif cmd[0] == "pop":
        # 스택의 길이가 0이상일때만
        if len(im_stack) > 0:
            print(im_stack.pop())
        # 스택의 길이가 0이면
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(im_stack))
    elif cmd[0] == "empty":
        if len(im_stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(im_stack) > 0:
            print(im_stack[-1])
        else:
            print(-1)
