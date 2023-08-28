import sys
input = sys.stdin.readline
N=int(input())
l=[]
for _ in range(N):
    l.append(tuple(map(int, input().split())))
    
l.sort(key = lambda x : (x[1],x[0]))

for next in l:
    print(*next)