### 촌수 계산 (S2)
import sys
input = sys.stdin.readline
from collections import deque
V = int(input())
s, e = map(int, input().split())
E = int(input())
G = [[] for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [-1] * (V+1)
def bfs(s, e):
    queue = deque()
    queue.append(s)
    visited[s] = 0
    while queue:
        now = queue.popleft()
        if now == e:
            break 
        for next in G[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)
    return visited[e]

print(bfs(s, e))
