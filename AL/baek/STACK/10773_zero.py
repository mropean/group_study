import sys
K = int(sys.stdin.readline())

im_stack = []
for i in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        # 0 일때 제
        im_stack.pop()
    else:
        # 0 아닐때 추가
        im_stack.append(num)

print(sum(im_stack))
