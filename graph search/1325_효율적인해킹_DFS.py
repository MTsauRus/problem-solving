### 효율적인 해킹(S1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, (input().split()))
    G[b].append(a) # 거꾸로 그래프에 넣음, unidirectional

# def dfs(v):
#     visited[v] = 1
#     for next in G[v]:
#         if visited[next] == 0:
#             dfs(next)

def dfs(v):
    visited = [0] * (V+1)
    stack = []
    stack.append(v)
    while stack:
        now = stack.pop() 
        visited[now] = 1    
        for next in G[now]:
            if visited[next] == 0:
                stack.append(next)
                visited[next] = 1 

    return visited  
            
max = 0
ans = []
#visited = [0] * (V+1)
for i in range(1, V+1):
    if len(G[i]) != 0:
        #visited = [0] * (V+1)
        visited = dfs(i)
        if sum(visited) > max:
            ans.clear()
            ans.append(i)
            max = sum(visited)
        elif sum(visited) == max:
            ans.append(i)
        
        else:
            continue
            

ans.sort()
print(*set(ans))

