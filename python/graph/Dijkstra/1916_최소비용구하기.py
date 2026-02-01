### 최소비용 구하기 (G5)
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

V = int(input())
E = int(input())
G = [[] for _ in range(V+1)]
cost = [sys.maxsize for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    G[a].append((w, b))
    
start, end = map(int, input().split())

def dijkstra(start, end):
    queue = []
    heappush(queue, start)
    cost[start[1]] = 0
    while queue:
        now_w, now_v = heappop(queue)
        if now_v == end:
            return 
        for next in G[now_v]:
            next_w, next_v = next[0], next[1] # next_weight, next_vertex
            if cost[next_v] > cost[now_v] + next_w:
                cost[next_v] = cost[now_v] + next_w
                heappush(queue, (cost[next_v], next_v))

dijkstra((0, start), end)
print(cost[end])