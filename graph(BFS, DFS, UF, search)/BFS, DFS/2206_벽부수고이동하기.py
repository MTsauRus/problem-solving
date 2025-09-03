### 벽 부수고 이동하기 (G3)
### 그래프, dfs

import sys
from collections import deque
input = sys.stdin.readline

X, Y = map(int, input().split())
G = []
dist = [[1 for _ in range(Y)] for _ in range(X)]
dist[X-1][Y-1] = 1000001
dist_d = [[1 for _ in range(Y)] for _ in range(X)] # 벽을 부숴 이동한 거리
dist_d[X-1][Y-1] = 1000001
for i in range(X):
    G.append(list(map(int, input().strip())))
    
# 0: 가지 않은 곳
# 1: 벽
# 2: 부숴서 간 곳
# 3: 부수지 않고 간 곳

def bfs(G, s1, s2):
    queue = deque()
    queue.append([s1, s2, 3])
    G[s1][s2] = 3 # 방문체크
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if z == 1 or z == 2: # 벽을 이미 부순 경우 한 번도 가지 않은 곳만 갈 수 있음.
                if 0 <= nx < X and 0 <= ny < Y and G[nx][ny] == 0:
                    G[nx][ny] = 2
                    queue.append([nx, ny, 2])
                    dist_d[nx][ny] = dist_d[x][y] + 1 # 이전 벽 부숴서 온 거리 + 1
                    
            elif z == 3: # 벽을 아직 부수지 않은 경우, 벽을 부수고 도달한 좌표를 포함할 수 있음.
                if (0 <= nx < X and 0 <= ny < Y) and G[nx][ny] in [0, 2]:
                    G[nx][ny] = 3
                    queue.append([nx, ny, 3])
                    dist[nx][ny] = dist[x][y] + 1
                    # 벽을 부수지 않았으므로 새 벽을 부술 수 있음
                    
                elif (0 <= nx < X and 0 <= ny < Y) and G[nx][ny] == 1:
                    # G[nx][ny] = 2 
                    # 벽은 그대로 벽으로 둬도 된다. 나중에 도달한 기회 있는 친구가 다음 Q에 넣어봤자 
                    # 이미 먼저 벽을 뚫은 친구 때문에 그 주변이 다 2이므로 거기서 bfs가 끝남. 
                    queue.append([nx, ny, 2])
                    # 이전 칸이 벽을 부수지 않고 도달한 칸이므로 dist[x][y] 사용
                    dist_d[nx][ny] = dist[x][y] + 1 

bfs(G, 0, 0)
ans = min(dist[X-1][Y-1], dist_d[X-1][Y-1])
if X == 1 and Y == 1:
    print(1)
elif ans == 1000001:
    print(-1)
else:
    print(ans)