### 최단경로 (G4)
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
G = [[] for _ in range(V+1)]
dist = [sys.maxsize] * (V+1)
for i in range(E):
    a, b, w = map(int, input().split())
    G[a].append((w, b))
                
def dijkstra(start):
    dist[start[1]] = 0
    queue = []
    heapq.heappush(queue, start)
    while queue:
        now = heapq.heappop(queue)
        for next in G[now[1]]:
            if dist[next[1]] > dist[now[1]] + next[0]:
                dist[next[1]] = dist[now[1]] + next[0]
                heapq.heappush(queue, (dist[next[1]], next[1]))
        
dijkstra((0, start))
for i in range(1, V+1):
    if dist[i] == sys.maxsize:
        print("INF")
    else:
        print(dist[i])