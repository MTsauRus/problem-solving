### 오민식의 고민 (P5)
import sys
input = sys.stdin.readline
minsize = -sys.maxsize

V, start, end, E = map(int, input().split())
edge = []
G = [[] for _ in range(V)]
cost = [minsize] * (V)

for _ in range(E):
    a, b, w = map(int, input().split())
    edge.append([a, b, -w])
    G[a].append(b)
    
earn = list((map(int, input().split())))

for i in range(V):
    for next in edge:
        if next[1] == i:
            next[2] += earn[i]

cost[start] = earn[start]
for i in range(E-1):
    for a, b, w in edge:
        if cost[a] != minsize and cost[b] < cost[a] + w:
            cost[b] = cost[a] + w
        
isCycle = False
for i in range(E): # 양수 사이클 확인
    for a, b, w in edge:
        if cost[a] != minsize and cost[b] < cost[a] + w:
            cost[b] = sys.maxsize

if cost[end] == minsize:
    print("gg")
elif cost[end] == sys.maxsize:
    print("Gee")
else:
    print(cost[end])
    
