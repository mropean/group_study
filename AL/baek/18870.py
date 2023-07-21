import sys
_ = sys.stdin.readline()
list_ = list(map(int, sys.stdin.readline().strip().split(" ")))

dict_ = {}
count = 0
for i in sorted(list_):
    if i not in dict_.keys():
        dict_[i] = count
        count += 1
        
for i in list_:
    print(dict_[i], end = " ")
