### swea 1226. 미로1 (D4)
### bfs/dfs

import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(1, 11):
    ans = 0
    t = int(input())
    maze = []
    for i in range(16):
        maze.append(list(map(int, input().strip())))

    dq = deque()
    dq.append((1, 1))
    
    while dq:
        if ans == 1:
            break
        next = dq.popleft()
        x, y = next[0], next[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[nx][ny] == 0:
                    maze[nx][ny] = -1 # 방문처리
                    dq.append((nx, ny))
                elif maze[nx][ny] == 3:
                    ans = 1
                    break

    print(f"#{t} {ans}")