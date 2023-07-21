def solution(genres, plays):
    count_dict_ = {}
    index_dict_ = {}
    answer = []
    for index, key_value in enumerate(zip(genres, plays)):
        if count_dict_.get(key_value[0]) == None:
            count_dict_[key_value[0]] = key_value[1]
            index_dict_[key_value[0]] = [index]
        else:
            count_dict_[key_value[0]] += key_value[1]
            index_dict_[key_value[0]].append(index)

    ranked_ = sorted(count_dict_.items(), key=lambda x: x[1], reverse=True)

    for i, _ in ranked_:
        if len(index_dict_[i]) > 1:
            m = 2
            index_rank = [None, None]
        else:
            m = 1
            index_rank = [None]

        for n in range(m):
            max_ = 0
            max_ind = -1
            del_ind = -1
            for j in range(len(index_dict_[i])):

                if plays[index_dict_[i][j]] > max_:
                    max_ = plays[index_dict_[i][j]]
                    max_ind = index_dict_[i][j]
                    del_ind = j

            index_rank[n] = max_ind
            del index_dict_[i][del_ind]

        answer.extend(index_rank)
            
    return answer
