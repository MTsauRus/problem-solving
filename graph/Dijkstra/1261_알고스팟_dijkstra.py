### 1261. 알고스팟 (G4)
### 다익스트라 버전
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

C, R = map(int, input().split())
G = []
for i in range(R):
    G.append(list(map(int, input().strip())))

dist = [[float('inf') for _ in range(C)] for _ in range(R)]
queue = [[0, 0, 0]] # dist, x, y
dist[0][0] = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while queue:
    now_dist, x, y = heappop(queue)
    if now_dist > dist[x][y]:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            next_dist = now_dist + G[nx][ny]
            if next_dist < dist[nx][ny]:
                dist[nx][ny] = next_dist
                heappush(queue, [next_dist, nx, ny])

print(dist[R-1][C-1])