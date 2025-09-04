### 특정한 최단 경로 (G4)
### 다익스트라, 그래프

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append([e, w])
    G[e].append([s, w])
    
v1, v2 = map(int, input().split()) # 반드시 지나야 하는 정점

def dijkstra(s):
    queue = [[0, s]] # 거리, 시작노드
    dist = [float('inf')] * (V+1)
    dist[s] = 0
    
    while queue:
        now_dist, now_node = heappop(queue)
        if now_dist > dist[now_node]: continue # 새로 꺼낸 웨이트가 최소거리보다 크면 볼 필요 없음
        
        for next_node, next_weight in G[now_node]:
            new_dist = dist[now_node] + next_weight
        
            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heappush(queue, [new_dist, next_node])
    return [dist[0]]+[dist[1]]+[dist[v1]]+[dist[v2]]+[dist[V]] # 이 네 값만 필요함 
                
# 1 -> v1 -> v2 -> V or 1 -> v2 -> v1 -> V
D = []
for i in [0, 1, v1, v2, V]:
    D.append(dijkstra(i))


ans = min(D[1][2] + D[2][3] + D[3][4], D[1][3] + D[3][2] + D[2][4])
if ans == float('inf'):
    print(-1)
else:
    print(ans)
