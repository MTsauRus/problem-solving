import sys
input = sys.stdin.readline

N = int(input())
l = []
for i in range(N):
    member = list(input().split())
    member.append(i)
    l.append(member)

l.sort(key = lambda x : (int(x[0]), x[2]))

for next in l:
    print(next[0], next[1])
