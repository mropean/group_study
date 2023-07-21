import sys

# Merge (slice는 메모리 효율이 좋지 않다는 점 생각.)
def SortNMerge(list_1, list_2):
    global find, count, answer
    list_T = []
    list_1_index, list_2_index = 0, 0
    
    while (list_1_index < len(list_1)) & (list_2_index < len(list_2)):
        if list_1[list_1_index] > list_2[list_2_index]:
            count += 1
            if count == find:
                answer = list_2[list_2_index]
            list_T.append(list_2[list_2_index])
            list_2_index += 1
        else:
            count += 1
            if count == find:
                answer = list_1[list_1_index]
            list_T.append(list_1[list_1_index])
            list_1_index += 1
            
    while list_2_index < len(list_2):
            count += 1
            if count == find:
                answer = list_2[list_2_index]
            list_T.append(list_2[list_2_index])
            list_2_index += 1
            
    while list_1_index < len(list_1):
            count += 1
            if count == find:
                answer = list_1[list_1_index]
            list_T.append(list_1[list_1_index])
            list_1_index += 1
    
    return list_T
    
def MergeSort(list_):
    ## Divide
    # 리스트의 원소가 1개라면
    if len(list_) < 2:
        return list_
    
    # 리스트를 절반으로 나누기
    if len(list_) % 2 == 1:
        middle = len(list_) // 2 + 1
    else:
        middle = len(list_) // 2
    # 
    list_L = MergeSort(list_[:middle])
    list_R = MergeSort(list_[middle:])    
    
    ## Sort & Merge
    return SortNMerge(list_L, list_R)

count = 0
answer = -1
_, find = list(map(int, sys.stdin.readline().split()))
MergeSort(list(map(int,sys.stdin.readline().split())))

print(answer)

