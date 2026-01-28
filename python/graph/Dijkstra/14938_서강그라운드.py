### 서강그라운드 (G4)
### 그래프, 다익스트라
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

V, scope, E = map(int, input().split())
items = [0] + list(map(int, input().split())) # 맨 앞에 0 삽입
G = [[] for _ in range(V+1)]
dist = [float('inf')] * (V+1)
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append([e, w])
    G[e].append([s, w])

def dijkstra(start):
    dist[start] = 0
    queue = [[0, start]] # 거리, 정점번호
    while queue:
        dist_now, now = heappop(queue)
        if dist_now > dist[now]: # 새로 꺼내온 노드가 이미 저장된 거리보다 큰 경우 무시
            continue # 돌아온 길은 볼 필요도 없다는 의미
        
        for next, weight in G[now]: # now의 자식 노드들의 다음 정점 번호 및 거리
            
            if dist[next] > dist_now + weight: # 다음 정점까지의 최소 거리보다 현재 거리 + 다음 노드 길이가 작다면
                dist[next] = dist_now + weight # 거리를 새로 업데이트하고
                heappush(queue, [dist_now + weight, next]) # 새 거리를 포함한 정점번호를 다음 큐에 넣자.
           
ans = [0] * (V+1)
for i in range(1, V + 1):
    dijkstra(i)
    for j in range(1, V + 1):
        if dist[j] <= scope: # 방문 가능하다면
            ans[i] += items[j]
    
    dist = [float('inf')] * (V+1)

print(max(ans))