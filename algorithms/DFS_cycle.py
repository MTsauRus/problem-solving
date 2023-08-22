### DFS 활용하여 싸이클 찾기
#1) 단방향 그래프
V, E = map(int, input().split())

def detect_uni():
    unidirectional = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        unidirectional[a].append(b)
    visited_uni = [False] * (V + 1)
    finished_uni = [False] * (V + 1)

    global cycle_uni
    cycle_uni = 0
    # dfs, 단방향, 연결 그래프의 사이클 찾기
    def dfs_unidirectional(v):
        global cycle_uni
        visited_uni[v] = True
        for next in unidirectional[v]:
            if not visited_uni[next]:
                dfs_unidirectional(next)
            elif not finished_uni[next]:
                cycle_uni += 1
        finished_uni[v] = True

    dfs_unidirectional(1)
    print(cycle_uni)


#_______________________________________
# 2. bidirectional
def detect_bi():
    bidirectional = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        bidirectional[a].append(b)
        bidirectional[b].append(a)
    visited_bi = [False] * (V + 1)
    
    global cycle_bi
    cycle_bi = False
    
    def dfs_bidirectional(v, parent):
        global cycle_bi
        visited_bi[v] = True
        for next in bidirectional[v]:
            if not visited_bi[next]:
                dfs_bidirectional(next, v) 
            elif parent != next:
                cycle_bi =  True

    dfs_bidirectional(1, -1)
    

detect_bi()
print(cycle_bi)