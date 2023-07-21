def solution(nums):
    answer = 0
    set_ = set(nums)
    has_ = len(nums) // 2
    if len(set_) >= has_:
        answer = has_
    else:
        answer = len(set_)
    return answer
