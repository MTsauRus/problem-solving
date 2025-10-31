### 12834. 주간미팅 (G4)
### 다익스트라
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, V, E = map(int, input().split())
end1, end2 = map(int, input().split())
Ns = list(map(int, input().split()))
    
G = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append([e, w])
    G[e].append([s, w])
    
def dijkstra(s, e):
    dist = [float('inf') for _ in range(V+1)]
    dist[s] = 0
    queue = [[0, s]]
    
    while queue:
        now_dist, now = heappop(queue)
        if now_dist > dist[now]:
            continue
        
        for next in G[now]:
            next_node, next_weight = next[0], next[1]
            next_dist = now_dist + next_weight
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heappush(queue, [next_dist, next_node])
    
    return dist[e]

ans = 0

for i in range(N):
    now = Ns[i]
    dist1 = dijkstra(now, end1)
    if dist1 == float('inf'):
        ans -= 1
    else:
        ans += dist1
    
    dist2 = dijkstra(now, end2)
    if dist2 == float('inf'):
        ans -= 1
    else:
        ans += dist2
    
print(ans)