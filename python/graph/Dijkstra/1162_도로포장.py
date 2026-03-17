### 1162. 도로포장 (P5)
### 다익스트라
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E, K = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append((w, e))
    G[e].append((w, s))

# 2차원 dist[node][K]    
dist = [[float('inf')]*(K+1) for _ in range(V+1)]
dist[1][0] = 0
pq = []
# (w, v, k)
heappush(pq, (0, 1, 0))

while pq:
    cw, cv, ck = heappop(pq)
    if dist[cv][ck] < cw: continue
    
    for nw, nv in G[cv]:
        # 포장 x
        next_dist = cw + nw
        if dist[nv][ck] > next_dist:
            dist[nv][ck] = next_dist
            heappush(pq, (next_dist, nv, ck))
        
        # 포장 o
        if ck < K:
            next_dist = cw
            if dist[nv][ck+1] > next_dist:
                dist[nv][ck+1] = next_dist
                heappush(pq, (next_dist, nv, ck+1))
    
print(min(dist[V]))