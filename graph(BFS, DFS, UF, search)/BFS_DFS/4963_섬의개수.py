### 섬의 개수 (S2)
import sys
input = sys.stdin.readline
from collections import deque

def bfs(a):
    global ans
    ans += 1
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    queue = deque()
    x, y = a[0], a[1]
    visited[x][y] = True
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny] and G[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = True

        
while True:
    col, row = map(int, input().split())
    if col == 0 and row == 0:
        break
    G = []
    global ans
    ans = 0
    for i in range(row):
        G.append(list(map(int, input().split())))
    visited = [[False for i in range(col)] for j in range(row)]
    for r in range(row):
        for c in range(col):
            if G[r][c] == 1 and not visited[r][c]:
                bfs([r, c])
                
    print(ans)
