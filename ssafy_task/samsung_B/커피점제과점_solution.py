from heapq import heappush, heappop
V = 0
E = 0
G = []
ans = float('inf')
def init(N, K, sBuilding, eBuilding, mDistance):
    global V, E, G
    V = N
    E = K
    G = [[] for _ in range(V)]
    
    for i in range(K):
        G[sBuilding[i]].append((mDistance[i], eBuilding[i]))
        G[eBuilding[i]].append((mDistance[i], sBuilding[i]))


def add(sBuilding, eBuilding, mDistance):
    global G
    G[sBuilding].append((mDistance, eBuilding))
    G[eBuilding].append((mDistance, sBuilding))

# M, P <= 1000
def calculate(M, mCoffee, P, mBakery, R):
    global ans
    
    ans = float('inf')
    # 커피숍 출발
    dist_cof = [float('inf')] * (V)
    # 베이커리 출발
    dist_bak = [float('inf')] * (V)

    isCoffee = [False] * V
    isBakery = [False] * V
    pq = [] # (weight, v, 시작점 -> 0이면 커피, 1이면 베이커리)
    for m in mCoffee:
        heappush(pq, (0, m, 0))
        dist_cof[m] = 0
        isCoffee[m] = True
    # 모든 베이커리를 시작 지점으로
    for p in mBakery:
        heappush(pq, (0, p, 1))
        dist_bak[p] = 0
        isBakery[p] = True
    
    while pq:
        cw, cv, type = heappop(pq)
        if cw>R: continue
        # 커피숍 출발 노드
        if not type: 
            if dist_cof[cv] < cw: continue
        
        # 베이커리 출발노드
        else:
            if dist_bak[cv] < cw: continue
        
        for nw, nv in G[cv]:
            next_dist = cw + nw
            # 허용 가능 거리보다 더 가야한다면 패스
            if next_dist > R: continue
            
            # 커피출발
            if not type:
                if isBakery[nv]:
                    ans = min(ans, dist_cof[nv] + dist_bak[nv])
                    continue
                
                if dist_cof[nv] <= next_dist: continue
                dist_cof[nv] = next_dist
                heappush(pq, (next_dist, nv, type))
            else:
                if isCoffee[nv]:
                    ans = min(ans, dist_cof[nv] + dist_bak[nv])
                    continue
                
                if dist_bak[nv] <= next_dist: continue
                dist_bak[nv] = next_dist
                heappush(pq, (next_dist, nv, type))

    ans = float('inf')
    for i in range(V):
        if isCoffee[i] or isBakery[i]:
            continue
        ans = min(ans, dist_bak[i] + dist_cof[i])
    
    return -1 if ans == float('inf') else ans