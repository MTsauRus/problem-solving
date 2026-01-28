### 1238. 파티 (G3)
### 그래프 탐색, 다익스트라?
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

V, E, X = map(int, input().split())
G = [[] for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, input().split())
    G[s].append([w, e]) # 가중치, 도착지
    
def dijkstra(s):
    queue = [[0, s]]
    dist = [float('inf') for _ in range(V+1)]
    dist[s] = 0
    
    while queue:
        now_dist, now_node = heappop(queue)
        if now_dist > dist[now_node]:
            continue # 새로 꺼낸 거리가 기존 최단거리보다 크면 패스
        for next in G[now_node]:
            next_weight, next_node = next[0], next[1]
            next_dist = next_weight + now_dist
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heappush(queue, [next_dist, next_node])
    return dist

dist_go = [0 for _ in range(V+1)]
for i in range(1, V+1):
    if i == X:
        dist_back = dijkstra(i)
    else:
        dist_go[i] = dijkstra(i)[X]
    
ans = 0
for i in range(1, V+1):
    ans = max(ans, dist_go[i] + dist_back[i])

print(ans)