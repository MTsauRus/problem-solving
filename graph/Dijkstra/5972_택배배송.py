### 택배 배송 (G5)
### 다익스트라

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append([e, w])
    G[e].append([s, w])
    
def dijkstra(s, e):
    dist = [float('inf')] * (V+1)
    queue = [[0, s]] # weight, node
    dist[s] = 0
    
    while queue:
        now_weight, now_node = heappop(queue)
        if now_weight > dist[now_node]: continue
        
        for next_node, next_weight in G[now_node]:
            next_dist = next_weight + dist[now_node]
            
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heappush(queue, [next_dist, next_node])

    return dist[e]

print(dijkstra(1, V))