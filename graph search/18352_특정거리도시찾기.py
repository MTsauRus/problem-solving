### 특정 거리의 도시 찾기(S2)
import sys
input = sys.stdin.readline

V, E, dis, start = map(int, input().split())
D = [0 for _ in range(V+1)]
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    G[a].append(b)

def bfs(v):
    visited = [False] * (V+1)
    queue = []
    queue.append(v)
    while queue:
        now = queue.pop(0)
        visited[now] = True
        for next in G[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                D[next] += D[now] + 1
        if max(D) > dis:
            return

bfs(start)
cnt = 0
for i in range(len(D)):
    if D[i] == dis:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)

    
