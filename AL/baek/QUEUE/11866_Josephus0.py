import sys
N, K = list(map(int, sys.stdin.readline().split()))
# N명의 사람 리스트
temp = [ i+1 for i in range(N) ]

# N명의 사람이 나간 순서(순열) 큐
queue = []
# 나간 사람 대기열의 최대 값
goal = N
index_ = 0
while True:
    # 큐의 길이가 최대 값(처음 입력한 N값)이라면
    if len(queue) == goal:
        break

    # K 값일때의 사람 큐에 추가, 리스트에서 제거
    count = 1
    while True:
        # 리스트 인덱스(감소되는 거)가 현재 사람수 N과 같아졌을때.
        # 원형이니 다시 0으로 초기화 해줘야됨.
        if index_ == N:
           index_ = 0 

        # K 값에 왔을 때
        if count == K:
            # 해당 인덱스의 사람 큐에 추가
            queue.append(temp[index_])
            # 리스트에서 사람 제거
            temp = temp[:index_] + temp[index_+1:]
            # 리스트에서 사람수 1 감소
            N -= 1
            break
        else:
            # K값까지 count 증가, 인덱스 증
            count += 1
            index_ += 1

print(f"<{', '.join(map(str, queue))}>")
