import sys
string_ = sys.stdin.readline().strip()
set_ = set()

for i in range(1, len(string_)):
    for j in range(len(string_)):
        set_.add(string_[j:i+j])
        if j == len(string_)-i:
            break
set_.add(string_)
print(len(set_))
