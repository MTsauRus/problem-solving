### 최소비용 구하기2 (G3)
### 다익스트라
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append([e, w])

start, end = map(int, input().split())

def dijkstra(s, e):
    dist = [float('inf')] * (V+1)
    dist[s] = 0
    prev_node = [-1 for _ in range(V + 1)] # 각 정점으로 가는 루트
    queue = [[0, s]] # dist, node
    while queue:
        now_dist, now_node = heappop(queue)
        if now_dist > dist[now_node]: continue # 새로 뽑은 노드가 너무 크다면 볼 필요 x
        
        for next_node, next_weight in G[now_node]:
            next_dist = now_dist + next_weight
            
            if dist[next_node] > next_dist: 
                dist[next_node] = next_dist
                heappush(queue, [next_dist, next_node])
                # now_node -> next_node 경로를 저장
                # next_node는 now_node의 다음 노드임. 즉, 경로임. 
                prev_node[next_node] = now_node

    return dist, prev_node

dist, prev_node = dijkstra(start, end)
ans = [end]
tmp = end
while True:
    ans.append(prev_node[tmp])
    tmp = prev_node[tmp]
    if tmp == start:
        break
print(dist[end])
print(len(ans))
print(*ans[::-1])