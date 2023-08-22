### 효율적인 해킹 BFS 풀이
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
G =  [[] for _ in range(V+1)]
reliance = [0 for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)

def bfs(v):
    queue = []
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.pop(0)
        for next in G[now]:
            if not visited[next]:
                visited[next] = True
                reliance[next] += 1
                queue.append(next)
    return reliance

for i in range(1, V+1):
    visited = [False] * (V+1)
    bfs(i)

#max = max(reliance)
high = 0
for i in range(1, V+1):
    high = max(high, reliance[i])
flag = False
for i in range(1, V+1):
    if reliance[i] == high:
        print(i,end=" ")
        flag = True

if flag == False:
    print(-1)
    





    

