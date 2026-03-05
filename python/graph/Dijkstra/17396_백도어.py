### 17396. 백도어 (G5)
### 다익스트라
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
G = [[] for _ in range(V)]
dist = [float('inf')]*V

vis = list(map(int, input().split()))
vis[-1] = 0
for i in range(E):
    s, e, w = map(int, input().split())
    
    if vis[e] == 1 or vis[s] == 1:
        continue
    G[s].append((w, e))
    G[e].append((w, s))
    
pq = [(0, 0)]
dist[0] = 0
while pq:
    cw, cv = heappop(pq)
    
    if cw > dist[cv]: continue
    
    for nw, nv in G[cv]:
        next_dist = cw + nw
        if next_dist >= dist[nv]:
            continue
        
        dist[nv] = next_dist
        heappush(pq, (next_dist, nv))

print(-1 if dist[-1] == float('inf') else dist[-1])