### 1939_중량제한 (G3)
### 다익스트라 응용

"""
- 가중치를 음수로 만들어 max heap으로 바꿔야 함
- next_weight는 두 가중치 중 min. 병목을 구해야하므로
- weight 초기값은 음수 inf. '최대' 병목을 구해야하므로   
"""

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    G[s].append((e, w))
    G[e].append((s, w))
    
start, end = map(int, input().split())

weight = [-float('inf')]*(V+1)
weight[start] = 1000000001
pq = [(-1000000001, start)]

while pq:
    cw, cv = heappop(pq)
    cw = -cw
    
    # 현재 뽑아온 weight가 최대 weight보다 작다면 더이상 볼 필요 x 
    if cw < weight[cv]: continue
    
    for nv, nw in G[cv]:
        next_weight = min(cw, nw)
        if weight[nv] < next_weight:
            weight[nv] = next_weight
            heappush(pq, (-next_weight, nv))

print(weight[end])