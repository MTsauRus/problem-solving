### 5719. 거의 최단 경로 (P5)
### 다익스트라, 역추적

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

## 이거 bfs로 해도 됨~
def dfs(now):
    global skip
    if now == start: return
    
    for nw, nv in G_rev[now]:

        if skip[nv][now]: continue
        # 현재까지의 최단거리 == 이전까지의 최단거리 + nv->now 엣지의 nw
        if dist[now] == dist[nv] + nw:
            # 뒤집어서 체크해야 함
            skip[nv][now] = True
            dfs(nv)
    
while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0: break
    start, end = map(int, input().split())
    G = [[] for _ in range(V)]
    G_rev = [[] for _ in range(V)] # 역추적을 위한 반대그래프
    skip = [[False]*V for _ in range(V)] # 최단 경로를 구성하는 노드 여부
    dist = [float('inf')] * V
    dist_ans = [float('inf')] * V
    dist[start] = 0
    dist_ans[start] = 0
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s].append((w, e))
        G_rev[e].append((w, s))
    
    # 정방향 다익스트라    
    pq = [(0, start)]
    while pq:
        cw, cv = heappop(pq)
        if dist[cv] < cw: continue
        
        for nw, nv in G[cv]:
            next_dist = cw + nw
            if dist[nv] > next_dist:
                dist[nv] = next_dist
                heappush(pq, (next_dist, nv))
    
    # 역방향 dfs 최소 경로 추적
    dfs(end)
    # 시작지점 복원
    #skip[start] = False
    
    # 다시 다익스트라 시작
    pq = [(0, start)]
    while pq:
        cw, cv = heappop(pq)
        if dist_ans[cv] < cw: continue
        
        for nw, nv in G[cv]:
            # 다음 노드가 최단거리 구성에 포함되어 있다면 건너뜀
            if skip[cv][nv]: continue
            next_dist = cw + nw
            if dist_ans[nv] > next_dist:
                dist_ans[nv] = next_dist
                heappush(pq, (next_dist, nv))
    
    print(-1) if dist_ans[end] == float('inf') else print(dist_ans[end])