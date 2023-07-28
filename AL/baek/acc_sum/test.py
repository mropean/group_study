import sys
import string
 
s = input()
q = int(input())

char_list = {}
for char in string.ascii_lowercase:
    char_list[char] = [0]
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
        char_list[char].append(count)
print(char_list)
for _ in range(q):
    c, start, end = input().split()
    print(char_list[c][int(end)+1] - char_list[c][int(start)])
