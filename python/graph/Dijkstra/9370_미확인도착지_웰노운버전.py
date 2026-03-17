### 9370. 미확인 도착지 - 다른버전 (G2)
### 다익스트라
"""
이 문제의 경우, 반드시 지나야 하는 경로가 하나 뿐이다.
이 경우, 모든 엣지의 weight에 2를 곱해주고, 
반드시 지나야 하는 엣지의 weight에만 1을 빼준다. 
start에서 다익스트라를 딱 한 번 돌리고, 
특정 노드에서의 dist 값이 홀수라면 
이 노드를 가기 위한 최단경로에 반드시 지나야 하는 엣지가 포함되어 있음이 보장된다. 
"""

import sys
from heapq import heappush, heappop
input = sys.stdin.readline



def dijkstra(start):
    global G
    dist = [10e9] * (V+1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        cw, cv = heappop(pq)
        if dist[cv] < cw: continue
        
        for nw, nv in G[cv]:
            next_dist = cw + nw
            if dist[nv] > next_dist:
                dist[nv] = next_dist
                heappush(pq, (next_dist, nv))

    return dist

T = int(input())
for t in range(T):
    V, E, K = map(int, input().split())
    start, m1, m2 = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        if (s, e) == (m1, m2) or (s,e) == (m2, m1):
            w = w*2-1
        else:
            w = w*2
        G[s].append((w, e))
        G[e].append((w, s))
        
    goals = []
    for _ in range(K):
        goals.append(int(input()))

    dist_s = dijkstra(start)
    
    ans = []
    
    for next in goals:
        if dist_s[next]%2:
            ans.append(next)

    ans.sort()
    print(*ans)