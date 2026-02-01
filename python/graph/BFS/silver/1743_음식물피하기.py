### 1743. 음식물 피하기 (S1)
### BFS
import sys
input = sys.stdin.readline
from collections import deque

R, C, N = map(int, input().split())
G = [[0 for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(N):
    r, c = map(lambda x : int(x)-1, input().split())
    G[r][c] = 1 # 1: 장애물
    
ans = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def bfs(r, c):
    size = 1
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and G[nr][nc] == 1:
                size += 1
                visited[nr][nc] = True
                queue.append((nr, nc))
    
    return size

for i in range(R):
    for j in range(C):
        if G[i][j] == 1 and not visited[i][j]:
            ans = max(ans, bfs(i, j))

print(ans)