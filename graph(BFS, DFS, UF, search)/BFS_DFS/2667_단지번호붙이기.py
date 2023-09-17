### 단지번호붙이기 (S1)
import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
G = []
for i in range(N):
    tmp = list(map(int, input().strip()))
    G.append(tmp)

def bfs(v: list, level):
    cnt = 0 
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append(v)
    G[v[0]][v[1]] += level
    cnt += 1
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if G[nx][ny] == 1:
                    queue.append([nx, ny])
                    G[nx][ny] += level
                    cnt += 1
    return cnt

ans = []
level = 2
for i in range(N):
    for j in range(N):
        if G[i][j] == 1:
            cnt = bfs([i, j], level)
            ans.append((cnt, level))
            level += 1

print(len(ans))
ans.sort()
for next in ans:
    print(next[0])
