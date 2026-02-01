### 전쟁 - 전투 (S1)
import sys
input = sys.stdin.readline
from collections import deque

col, row = map(int, input().split())
G = []
for i in range(row):
    G.append(list(input().strip()))
global white, blue
white = 0
blue = 0
visited = [[False for _ in range(col)] for _ in range(row)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a):
    global white, blue
    queue = deque()
    cnt = 1
    x, y = a[0], a[1]
    color = G[x][y]
    queue.append([x, y])
    while queue:
        now = queue.popleft()
        x, y = now[0], now[1]
        for i in range(4):
            nx = x + dx[i]            
            ny = y + dy[i] 
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny] and G[nx][ny] == color:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1
    
    if color == 'W':
        white += cnt*cnt
    else:
        blue += cnt*cnt

for x in range(row):
    for y in range(col):
        if not visited[x][y]:
            visited[x][y] = True
            bfs([x, y])

print(white, blue)
                    
    
    