from collections import deque

priorities = [2, 1, 3, 2]
location = 2

answer = 0
queue = deque([(i, p) for i, p in enumerate(priorities)])


while queue:
    item = queue.popleft()
    if queue and max(queue, key=lambda x: x[1])[1] > item[1]:
        queue.append(item)
    else:
        answer += 1
        if item[0] == location:
            break

print(answer)
