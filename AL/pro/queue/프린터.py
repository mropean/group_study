def solution(priorities, location):
    answer = 0
    index_list = [i for i in range(len(priorities))]
    count = 0
    max_n = len(priorities)

    while count < max_n:
        if len(priorities) == 1:
            count += 1
            answer = count
            break
        elif priorities[0] < max(priorities[1:]):
            priorities.append(priorities[0])
            index_list.append(index_list[0])
            del priorities[0]
            del index_list[0]
        else:
            count += 1
            if index_list[0] == location:
                answer = count
                break
            else:
                del priorities[0]
                del index_list[0]
    
    return answer
