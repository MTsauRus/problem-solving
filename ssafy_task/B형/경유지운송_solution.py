from heapq import heappush, heappop
from itertools import permutations
G = []
N_nodes = 0

def init(N, K, sCity, eCity, mLimit):
    global G, N_nodes
    
    N_nodes = N
    G = [[] for _ in range(N)]
    
    for i in range(K):
        u = sCity[i]
        v = eCity[i]
        w = mLimit[i]
        G[u].append((w, v))
        G[v].append((w, u))
        
def add(sCity, eCity, mLimit):
    G[sCity].append((mLimit, eCity))
    G[eCity].append((mLimit, sCity))
    
def get_widest_paths(start):
    #dist: 최대 중량
    dist = [-1] * N_nodes
    dist[start] = float('inf')
    
    # 최대 힙
    pq = [(-float('inf'), start)]
    
    while pq:
        cw, cv = heappop(pq)
        cw = -cw
        
        # 현재 weight가 사전에 기록된 최댓값보다 작다면 볼 필요 없음
        if dist[cv] > cw:
            continue
        
        for nw, nv in G[cv]:
            # 현재 w와 다음 w중 작은 값이 병목
            next_limit = min(cw, nw)
            
            # 다음 노드의 최대 병목보다 더 크다면 업데이트
            if next_limit > dist[nv]:
                dist[nv] = next_limit
                heappush(pq, (-next_limit, nv))
                
    return dist

def calculate(sCity, eCity, M, mStopover):
    
    targets = [sCity] + mStopover
    dist_map = {}
    
    # 필요한 정점들에 대한 다익스트라
    for t in targets:
        dist_map[t] = get_widest_paths(t)
            
    max_final_weight = -1
    
    # 가능한 모든 방문 순서
    for p in permutations(mStopover):
        current_loc = sCity
        path_min_weight = float('inf')
        
        for next_stop in p:
            weight = dist_map[current_loc][next_stop]
            
            # 못가면 다음 순열로
            if weight == -1:
                path_min_weight = -1
                break
            
            # 현재 순열의 최소 병목 업데이트
            path_min_weight = min(path_min_weight, weight)
            current_loc = next_stop
        
        # 마지막 순열에서 도착지점까지의 구간
        if path_min_weight != -1:
            weight_to_end = dist_map[current_loc][eCity]
            if weight_to_end == -1:
                path_min_weight = -1
            else:
                path_min_weight = min(path_min_weight, weight_to_end)
                
        
        max_final_weight = max(max_final_weight, path_min_weight)
    
    return max_final_weight