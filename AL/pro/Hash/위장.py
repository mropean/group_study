def solution(clothes):
    answer = 1
    dict_ = dict()
    for i, j in clothes:
        if dict_.get(j) != None:
            dict_[j] += 1
        else:
            dict_[j] = 1

    list_t = list(dict_.values())

    for i in list_t:
        answer *= (i + 1)
                
    return answer-1
