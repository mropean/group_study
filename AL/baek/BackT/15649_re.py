from sys import stdin

def back(list_, M, N):
    if len(list_) == M:
        print(" ".join(map(str, list_)))
        return
    else:
        for i in range(1, N+1):
            if i not in list_:
                list_.append(i)
                back(list_, M, N)
                list_.pop()
        
    
N, M = list(map(int, stdin.readline().split()))
list_ = []
back(list_, M, N)    