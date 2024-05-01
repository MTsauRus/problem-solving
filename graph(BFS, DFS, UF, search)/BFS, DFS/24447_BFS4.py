### BFS4(S2)
import sys
input = sys.stdin.readline
from collections import deque

V, E, s = map(int, input().split())
G = [[] for i in range(V+1)]
for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
dist = [-1] * (V+1)
seq = [0] *(V+1)
Q = deque()
Q.append(s)
dist[s] = 0
num = 1
while Q:
    now = Q.popleft()
    seq[now] = num
    num += 1
    for next in G[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            Q.append(next)

ans = 0
for i in range(1, V+1):
    ans += seq[i] * dist[i]
print(ans)
