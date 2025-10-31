### 숨바꼭질 3
### 다익스트라, bfs
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

a, b = map(int, input().split())
visited = [False for _ in range(100001)]
dist = [float('inf') for _ in range(100001)]

def dijkstra(a):
    queue = [[0, a]]
    dist[a] = 0
    
    while queue:
        dist_now, now = heappop(queue)
        
        if dist_now > dist[now]:
            continue
        
        if now*2 < 100001 and dist[now*2] > dist[now]:
            dist[now*2] = dist[now]
            heappush(queue, [dist[now], now*2])
        
        if now+1 < 100001 and dist[now+1] > dist[now] + 1:
            dist[now+1] = dist[now] + 1
            heappush(queue, [dist[now]+1, now+1])
    
        if now-1 >= 0 and dist[now-1] > dist[now] + 1:
            dist[now-1] = dist[now] + 1
            heappush(queue, [dist[now]+1, now-1])
            
dijkstra(a)
print(dist[b])