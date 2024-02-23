### 알고리즘 수업 - 너비 우선 탐색 3 (S2)
import sys
input = sys.stdin.readline
from collections import deque

V, E, s = map(int, input().split())
G = [[] for i in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
depth = [-1] * (V+1)
Q = deque()
Q.append(s)
depth[s] = 0
while Q:
    now = Q.popleft()
    for next in G[now]:
        if depth[next] == -1:
            depth[next] = depth[now] + 1
            Q.append(next)

for i in range(1, V+1):
    print(depth[i])