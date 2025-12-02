### 1520. 내리막길 (G3)
### 백트래킹, dfs << 안됨
### DP
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
G = []
for i in range(R):
    G.append(list(map(int, input().split())))
    
D = [[0 for _ in range(C)] for _ in range(R)] # D[r][c]: [r, c]->[R-1, C-1]로 가는 경우의 수
D[R-1][C-1] = 0




# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# R, C = map(int, input().split())
# G = []
# for i in range(R):
#     G.append(list(map(int, input().split())))
    
# ans = 0
# visited = [[False for _ in range(C)] for _ in range(R)]
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]

# def dfs(r, c):
#     global ans

#     if r == R-1 and c == C-1:
#         ans += 1
#         return
    
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
#             if G[r][c] > G[nr][nc]: # 다음칸이 더 작다면
#                 visited[nr][nc] = True
#                 dfs(nr, nc)
#                 visited[nr][nc] = False

# dfs(0, 0)
# print(ans)