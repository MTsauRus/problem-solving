### 17086. 아기 상어 2 (S2)
### BFS
import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
G = []
for i in range(R):
    G.append(list(map(int, input().split()))) 
start = deque()
dist = [[-1 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c] == 1:
            start.append([r,c])
            dist[r][c] = 0

ans = 0
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
def bfs(queue): 
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append([nx, ny])

ans = 0

bfs(start)

for r in range(R):
    for c in range(C):
        ans = max(ans, dist[r][c])
print(ans)