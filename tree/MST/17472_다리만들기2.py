### 다리 만들기 2 (G1)
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush

c, r = map(int, input().split())
G = []
for _ in range(c):
    G.append(list(map(int, input().split())))
    
def bfs(a, b):
    level = 2
    queue = deque()
    queue.append([a,b])
    G[a][b] = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if G[nx][ny] != -1:
                    if G[nx][ny] == 0:
                        queue.append([nx, ny])
                        G[nx][ny] = -1
                    else:
                        G[nx][ny] = level
                        queue.append([nx, ny])
        level += 1

bfs(0, 0)
print(G)