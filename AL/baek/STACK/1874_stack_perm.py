import sys
inp = sys.stdin.readline
n = int(inp()) # n의 값
a_list = [ int(inp()) for _ in range(n) ] # 만들고 싶은 수열
t_list = [ i+1 for i in range(n) ] # 1부터 n까지 리스트
temp = [] # 현재 대기열(스택)
answer = [] # 해당 대기열에 push, pop이 몇번 일어났는지

a_index = 0
t_index = 0

for i in t_list:
    temp.append(i)
    answer.append("+")
    if i == a_list[a_index]:
        for t_index in range(len(temp)-1, -1, -1):
            if temp[t_index] == a_list[a_index]:        
                temp.pop()
                answer.append("-")
                a_index += 1
            else:
                break

if len(temp) > 0:
    print("NO")
else:
    for i in answer:
        print(i)
