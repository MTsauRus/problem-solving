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


def calculate(M, mCoffee, P, mBakery, R):

    # 커피 출발 / 베이커리 출발 별 거리 리스트 분리
    dist_cof = [float('inf')] * V
    dist_bak = [float('inf')] * V

    # 커피 / 베이커리 여부 판단 리스트 선언
    isCoffee = [False] * V
    isBakery = [False] * V
    pq = [] 
    
    # (weight, node, 커피/베이커리 여부)
    for m in mCoffee:
        heappush(pq, (0, m, 0))
        dist_cof[m] = 0
        isCoffee[m] = True
        
    for p in mBakery:
        heappush(pq, (0, p, 1))
        dist_bak[p] = 0
        isBakery[p] = True
        
    ans = float('inf')

    while pq:
        cw, cv, type = heappop(pq)
        # 뽑아온 weight가 R보다 크거나 ans보다 크면 볼 필요가 없음
        if cw > R or cw >= ans: 
            continue
            
        if not type: # 커피숍 출발
            # 기본 가지치기
            if dist_cof[cv] < cw: continue
            
            # 일반 노드이고, 커피에서 출발했고, 베이커리 -> 현재노드로 오는 길이 R 이하로 유효하다면
            if not isCoffee[cv] and not isBakery[cv] and dist_bak[cv] <= R:
                # cw (커피숍 -> 현재노드까지 오는 거리) + dist_bak[cv] (베이커리에서 현재 노드까지 오는 거리)
                # 이게 ans보다 작으면 업뎃해주자. 
                if cw + dist_bak[cv] < ans:
                    ans = cw + dist_bak[cv]
                    # 이때 pq에 넣지 않음. 이미 완성된 경로이고, 추가 탐색은 이 경로보다 반드시 긺
                    
        else: # 베이커리 출발
            if dist_bak[cv] < cw: continue
            
            if not isCoffee[cv] and not isBakery[cv] and dist_cof[cv] <= R:
                if cw + dist_cof[cv] < ans:
                    ans = cw + dist_cof[cv]
                    
        # 다음 노드 확인 과정
        for nw, nv in G[cv]:
            next_dist = cw + nw
            # 다음 노드까지 가는 거리가 R보다 크거나 ans보다 크면 볼 필요 없음
            if next_dist > R or next_dist >= ans: 
                continue
                
            # 커피 / 베이커리 출발지 분리해서 생각
            if not type:
                if dist_cof[nv] <= next_dist: continue
                dist_cof[nv] = next_dist
                heappush(pq, (next_dist, nv, type))
            else:
                if dist_bak[nv] <= next_dist: continue
                dist_bak[nv] = next_dist
                heappush(pq, (next_dist, nv, type))

    return -1 if ans == float('inf') else ans