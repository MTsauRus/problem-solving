from heapq import heappush, heappop
V = 0
E = 0
G = []

def init(N, K, sBuilding, eBuilding, mDistance):
    global V, E, G
    V = N
    E = K
    G = [[] for _ in range(V)]
    
    for i in range(K):
        G[sBuilding[i]].append((mDistance[i], eBuilding[i]))
        G[eBuilding[i]].append((mDistance[i], sBuilding[i]))



def add(sBuilding, eBuilding, mDistance):
	G[sBuilding].append((mDistance, eBuilding))
	G[eBuilding].append((mDistance, sBuilding))
 

# M, P <= 1000
def calculate(M, mCoffee, P, mBakery, R):
    dist = [float('inf')] * (V)
    pq = []
    # 모든 커피숍을 시작 지점으로
    for m in range(M):
        heappush(pq, (0, mCoffee[m]))
        dist[m] = 0
    
    while pq:
        cw, cv = heappop(pq)
        if dist[cv] < cw:
            continue
        
        for nw, nv in G[cv]:
            next_dist = cw + nw
            # 어차피 첫 조건에서 커피숍간 이동은 걸러지므로 따로 처리 x
            if dist[nv] > next_dist and next_dist <= R:
                dist[nv] = next_dist
                heappush(pq, (next_dist, nv))
        
    
    for p in range(P):
        if dist[p]
        
 