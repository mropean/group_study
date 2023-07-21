N = int(input())

answer = 0
if N % 5 == 0:
    answer = N // 5
elif (N % 5) % 3 == 0:
    answer = (N // 5) + ((N % 5) // 3)
elif ((N % 5) + 5) % 3 == 0:
    if ((N % 5) + 5) > N:
        answer = -1
    else:
        answer = ((N // 5) - 1) + (((N % 5) + 5) // 3)
elif ((N - 12) % 5) == 0:
    if N - 12 < 0:
        answer = -1
    else:
        answer = 4 + ((N - 12) // 5)
else:
    answer = -1

print(answer)
