### 1520. 내리막길 (G3)
### 백트래킹, dfs << 안됨
### DP + dfs
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

R, C = map(int, input().split())
G = []
for i in range(R):
    G.append(list(map(int, input().split())))
    
D = [[-1 for _ in range(C)] for _ in range(R)] # D[r][c]: [r, c]->[R-1, C-1]로 가는 경우의 수
D[R-1][C-1] = 1
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# -1: 방문 필요, 0: 이미 방문, 목적지까지 못감, 1이상: 목적지까지 가는 경로의 수
def dfs(r, c):
    if D[r][c] == 0:
        return 0
    elif D[r][c] > 0:
        return D[r][c]
    else:
        D[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] < G[r][c]:
                D[r][c] += dfs(nr, nc)
                
        return D[r][c]

print(dfs(0,0))