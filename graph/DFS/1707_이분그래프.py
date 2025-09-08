### 이분 그래프(G4)
import sys
input = sys.stdin.readline

N = int(input())
global bipartite
bipartite = True

def dfs(v):
    global visited
    global group_num
    visited[v] = group_num % 2
    group_num += 1
    global bipartite

    for next in G[v]:
        if visited[next] < 0:
            dfs(next)
        elif visited[next] == visited[v]:
            bipartite = False


for _ in range(N):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    global visited
    global group_num
    bipartite = True

    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    
    for i in range(1,  V+1):
        bipartite = True
        visited = [-(i + 1) for i in range(V+1)]
        group_num = 0
        dfs(i)
        if not bipartite:
            print("NO")
            break
    
    if bipartite:
        print("YES")
    


    

