import sys

def merge(s, e):
    list_T = []
    i, j = 0, 0
    
    while (i<len(s)) & (j<len(e)):
        if s[i]>e[j]:
            list_T.append(e[j])
            j+=1
        else:
            list_T.append(s[i])
            i+=1
    while (j<len(e)):
            list_T.append(e[j])
            j+=1
    while (i<len(s)):
            list_T.append(s[i])
            i+=1
    return list_T
    
def divide(list_):
    if len(list_) < 2:
        return list_
    
    middle = len(list_) // 2
    start = divide(list_[:middle])
    end = divide(list_[middle:])
    
    return merge(start, end)

N = sys.stdin.readline()
list_ = [int(sys.stdin.readline()) for i in range(int(N))]

list_ = divide(list_)

for i in list_:
    print(i)
