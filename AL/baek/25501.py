def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 0
    return recursion(s, 0, len(s)-1)

import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
count = 0

for i in data:
    print(isPalindrome(i), count)
