import sys
input = sys.stdin.readline

## 50점 이하
#S = input().split()[0]
#q = int(input())

#for _ in range(q):
#    c, s, e = input().split()
#    print(S[int(s):int(e)+1].count(c))

## 50점
#s = list(input().rstrip())
#n = int(input().rstrip())
#cList = [[0] * len(s) for _ in range(26)]

#for i in range(len(s)):
#    cList[ord(s[i])-ord('a')][i] += 1

#for _ in range(n):
#    c, start, end = input().split()
#    print(sum(cList[ord(c) - ord('a')][int(start):int(end)+1]))
    
S = list(input().split()[0])
q = int(input())

acc = [ [0] * len(S) for _ in range(26) ]

for i in range(len(S)):
    acc[ord(S[i]) - ord("a")][i] += 1

for i in range(26):
    for j in range(1, len(S)):
        acc[i][j] += acc[i][j-1]

for _ in range(q):
    c, s, e = input().split()
    num = acc[ord(c) - ord("a")][int(e)] - acc[ord(c) - ord("a")][int(s)]

    if S[int(s)] == c:
        num += 1

    print(num)
