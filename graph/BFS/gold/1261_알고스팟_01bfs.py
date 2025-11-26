### 1261. 알고스팟 (G4)
### 0-1 BFS
import sys
input = sys.stdin.readline
from collections import deque

C, R = map(int, input().split())
G = []
for i in range(R):
    G.append(list(map(int, input().strip())))
    
queue = deque([[0, 0]])
dist = [[-1 for _ in range(C)] for _ in range(R)]
dist[0][0] = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] == -1:
            if G[nx][ny] == 0:
                queue.appendleft([nx, ny])
                dist[nx][ny] = dist[x][y]
            else: # G[nx][ny] == 1
                queue.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1
                
print(dist[R-1][C-1])