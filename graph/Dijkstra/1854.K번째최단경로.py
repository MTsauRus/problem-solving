### K번째 최단경로 찾기 (P4)
import sys
from heapq import heappop, heappush
V, E, k = map(int, input().split())
G = [[] for _ in range(V+1)]
dist = [[sys.maxsize]*k for _ in range (V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    G[a].append((w, b)) # for Dijkstra, weight first
    
def dijkstra(start):
    queue = []
    heappush(queue, start)
    dist[start[1]][0] = 0
    while queue:
        cw, cv = heappop(queue)
        for next in G[cv]:
            nw, nv = next[0], next[1]
            next_dist = cw + nw

            if dist[nv][k-1] > next_dist:
                dist[nv][k-1] = next_dist    
                dist[nv].sort()
                heappush(queue, (next_dist, nv))
                
dijkstra((0, 1))
for i in range(1, V+1):
    if dist[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(dist[i][k-1])
        
