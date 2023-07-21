import sys
import re
inp = sys.stdin.readline

while True:
    in_ = inp()
    in_ = in_.strip("\n")
    if in_ == ".":
        break
    else:
        # 문자열에서 괄호만 남기기
        in_ = re.sub("[a-zA-Z0-9\w\s.]+", "", in_)

        flag = 0
        stack = []
        for i in in_:
            # 문자가 ( { [ 인경우엔 스택에 추가.
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                # 만약 문자열의 첫 문자인데 ) } ] 인 경우.
                # )(())(
                if (i == ")" or i == "}" or i == "]") and len(stack) == 0:
                    flag = 1
                    break
                # 괄호는 짝을 이루어야 한다.
                else:
                    # ) 인 경우 스택 마지막 인덱스는 ( 여야 한다.    
                    if i == ")":
                        # ({[([()
                        # 맞으면 스택에서 제거
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            flag = 1
                            break
                    elif i == "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            flag = 1
                            break
                    elif i == "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            flag = 1
                            break
                        
        # 게다가 스택에 남은 문자가 없어야지 완벽한 문자열이다.
        # (((( <- 와 같은 경우 방
        
        if flag == 0 and len(stack) == 0:
            print("yes")
        else:
            print("no")
