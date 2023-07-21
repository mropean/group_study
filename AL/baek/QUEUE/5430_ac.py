import sys
import re
from collections import deque
inp = sys.stdin.readline

# 테스트 케이스 갯수만큼
for _ in range(int(inp())):
    # 명령입력
    cmd = " ".join(inp().strip()).split() # RDD [R, D, D]
    # 원소 갯수
    n = int(inp())
    # 배열
    # ex) 문자열 "[1,2,3,4]"를 ['1', '2', '3', '4'] 리스트 형태로
    temp = re.sub("[^0-9,]+", "", inp()).split(',') 

    # 리스트에 들어있는 원소의 갯수가 1개 이상이라면 int형으로 변환
    #if len(temp[0]) > 0: # 
    #    temp = deque(map(int, temp))

    # 뒤집힌 상태인지 확인    
    r_flag = False # RDD

    # 원소의 갯수보다 "D" 명령이 많다면 오류.
    # 2 / DDD
    if n < cmd.count("D"):
        print("error")
        # 다음 테스트 케이스로
        continue
    
    # 배열에 들어있는 원소가 없고, "D" 명령도 없다면
    elif n == 0 and cmd.count("D") == 0:
        # 빈배열 출력
        print("[]")
        # 다음 테스트 케이스로
        continue

    else:
        # 명령의 순서대로
        for c in cmd: # R D D
            if c == 'R':
                if r_flag:
                    # 원래대로
                    r_flag = False
                else:
                    # 뒤집기
                    r_flag = True
            else:
                # 뒤집힌 상태라면
                if r_flag:
                    # 맨뒤 원소 버리기
                    # 1234 / 4321
                    temp.pop()
                # 뒤집힌 상태가 아니라면
                else:
                    # 1234 / 1
                    # 맨앞 원소 버리기
                    temp.popleft()
    # TRUE
    # RDDR / RDD 
    # 마지막으로 뒤집힌 상태로 끝났다면
    if r_flag:
        # 리스트 뒤집기
        temp.reverse()
    print(re.sub("[\s]","", str(list(temp))))
