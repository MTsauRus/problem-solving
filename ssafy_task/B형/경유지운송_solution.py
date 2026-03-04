G = []
dist = []

def init(N, K, sCity, eCity, mLimit):
    global G, dist
    G = [[] for _ in range(N)]
    dist = [[float('inf')*N] for _ in range(N)]
    
    for i in range(K):
        s = sCity[i]
        e = eCity[i]
        w = mLimit[i]
        G[s].append([w, e])
        G[e].append([w, s])
        
    def dijkstra(s, e):
        
        
    

    
    return G


def add(sCity, eCity, mLimit):
    
	return


def calculate(sCity, eCity, M, mStopover):
	return



init(10, 1, [1], [2], [3])
