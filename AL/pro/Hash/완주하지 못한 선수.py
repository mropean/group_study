from collections import Counter

def solution(participant, completion):
    answer = ''
    if len(set(participant) - set(completion)) == 1:
        return (set(participant) - set(completion)).pop()
    else:
        p_same =  Counter(participant).most_common()
        c_same = Counter(completion).most_common()
        return Counter(p_same + c_same).most_common()[-1][0][0]
    
