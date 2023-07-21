import sys
n = int(sys.stdin.readline())
list_N = sorted(list(map(int, sys.stdin.readline().split()))) # 정렬
m = int(sys.stdin.readline())
list_M = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    flag = 0
    start = 0
    end = n-1
    
    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2    
        # 원하는 값이 맞으면 1출력
        if list_M[i] == list_N[mid]:
            print(1, end="")
            flag = 1
            break
        ## 정렬이 이미 되어있는 상태
        # M리스트의 원소가 N리스트 중간값보다 작으면
        # 중간값의 왼쪽 인덱스가 끝 지점
        elif list_M[i] < list_N[mid]:
            end = mid-1
        # M리스트의 원소가 N리스트 중간값보다 크면
        # 중간값의 오른쪽 인덱스가 시작 지점
        else:
            start = mid+1
    # 값을 찾지 못했으면 0출력
    if flag == 0:
        print(0, end= "")

    if i+1 != m:
        print(" ", end="")

