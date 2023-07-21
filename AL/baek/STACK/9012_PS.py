import sys
K = int(sys.stdin.readline())

for _ in range(K):
    ps = " ".join(sys.stdin.readline()).split()
    # (의 갯수와 )의 갯수가 다른경우
    if ps.count("(") != ps.count(")"):
        print("NO")
        continue
    # )로 시작하는 경우
    elif ps[0] == (")"):
        print("NO")
        continue
    
    start = 0
    end = 0
    flag = 0
    
    for i in ps:
        if i == "(":
            start += 1
        
        else:
            end += 1
        # (로 시작하는 횟수가 )로 끝나는 횟수보다 크거나 같다.
        # 즉, )의 크기가 더크다면 잘못된 괄
        # 예를들어 ()))((
        # 위 괄호는 1, 2 조건을 만족하고. 아래의 조건을 만족하지 못한다.
        if start < end:
            print("NO")
            flag = 1
            break
        
    if flag != 1:
        print("YES")
