### 영상처리(S2)
import sys
from collections import deque
input = sys.stdin.readline

def avg(l):
    tmp = 0
    for i in l:
        tmp += i
    return tmp/len(l)

R, C = map(int, input().split())
G = []
for r in range(R):
    tmp = list(map(int, input().split()))
    tmp2 = []
    for i in range(0, C*3, 3):
        l = [tmp[i], tmp[i+1], tmp[i+2]]
        tmp2.append(avg(l))
    G.append(tmp2)

global ans
key = float(input())
visited = [[False for _ in range(C)] for _ in range(R)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(l):
    global ans
    a = l[0]
    b = l[1]
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and G[nx][ny] >= key:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    
                    
for r in range(R):
    for c in range(C):
        if G[r][c] >= key and not visited[r][c]:
            ans += 1
            bfs([r, c])

print(ans)
                    