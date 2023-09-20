### 쉬운 최단거리(S1)
import sys
input = sys.stdin.readline
from collections import deque

row, col = map(int, input().split())
G = []
for i in range(row):
    G.append(list(map(int, input().split())))

def bfs(x, y):
    visited = [[False for _ in range(col)] for _ in range(row)]
    ans = [[0 for _ in range(col)] for _ in range(row)]
    ans[x][y] = 0
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny] and G[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    ans[nx][ny] = ans[x][y] + 1
    return ans
for i in range(row):
    for j in range(col):
        if G[i][j] == 2:
            si, sj = i, j

ans = bfs(si, sj)

for i in range(row):
    for j in range(col):
        if ans[i][j] == 0:
            if G[i][j] == 1:
                ans[i][j] = -1
        
for next in ans:
    print(*next)
