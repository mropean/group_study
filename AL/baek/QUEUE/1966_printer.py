import sys
from collections import Counter
inp = sys.stdin.readline

# 테스트 케이스 횟수만
for _ in range(int(inp())):
    N, M = list(map(int, inp().split()))
    importance = list(map(int, inp().split()))

    if N == 1:
        print(1)
    else:
        # 각중요도를 인덱스값과 합침
        # 인덱스 값에서 M값을 찾아야함
        temp = [ (x, y) for x, y in enumerate(importance) ]

        flag = True
        counter = 1 # 문제. 몇번째로 출력되었니
        while flag:
            # 중요도만 추출
            temp_imp = list(map(lambda x : x[1], temp))
            # 중요도가 다 같으면
            if len(dict(Counter(temp_imp))) == 1:
                for x, y in temp:
                    # 내가 찾던 문서(인덱스)의 값(M) 일때 
                    if x == M:
                        print(counter)
                        flag = False
                        break
                    else:
                        counter += 1
            # 중요도가 다르면
            else:
                # 0번 인덱스에서
                _max = max(temp_imp)
                # 중요도 max값을 찾았으면
                if temp[0][1] == _max:
                    # 근데 그 값이 M일경우
                    if temp[0][0] == M:
                        print(counter)
                        flag = False
                    # 아니면 출력 count+1
                    else:
                        counter += 1
                        temp = temp[1:]
                # 0번 인덱스가 max값이 아니면
                # 첫번째 값을 맨뒤로
                else:
                    t = temp[1:]
                    t.extend(temp[:1])
                    temp = t
