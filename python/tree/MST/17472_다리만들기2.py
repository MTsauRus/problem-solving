### 다리 만들기 2 (G1)
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush

r, c = map(int, input().split())
visited = [[False for _ in range(c)] for _ in range(r)]
G = []
for _ in range(r):
    G.append(list(map(int, input().split())))
    
def bfs(a, b, level): # 섬 번호 매기기
    queue = deque()
    queue.append([a,b])
    visited[a][b] = True
    G[a][b] = level
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and G[nx][ny] == 1:
                    G[nx][ny] = level
                    visited[nx][ny] = True
                    queue.append([nx, ny])

lv = 1
for i in range(r):
    for j in range(c):
        if G[i][j] == 1 and not visited[i][j]:
            bfs(i, j, lv)
            lv += 1

bridged = [[False for _ in range(c)] for _ in range(r)] # 섬 내부에 대한 visited
bridges = [] # 다리 집합

def build_bridge(a, b):
    queue = deque()
    queue.append([a, b])
    bridged[a][b] = True
    bridge_len = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not bridged[nx][ny] and G[nx][ny] == 0:
                    bridge_len += 1
                    while True:
                        nx += dx[i]
                        ny += dy[i]
                        if not (0 <= nx < r and 0 <= ny < c): # 격자 범위를 벗어나면
                            break
                        elif G[nx][ny] == G[a][b]: # 같은 섬에 도착했다면
                            break
                        elif G[nx][ny] != 0: # 다음 섬에 도착하였다면
                            if bridge_len > 1:
                                heappush(bridges, [bridge_len, G[a][b], G[nx][ny]]) # [다리 길이, 시작 섬 번호, 끝 섬 번호]
                            break
                        else: # 바다라면 다리 길이를 늘린다. 
                            bridge_len += 1

                    bridge_len = 0
                else: # G[nx][ny]가 섬 내부일 경우
                    if not bridged[nx][ny]:
                        queue.append([nx, ny])
                        bridged[nx][ny] = True

for i in range(r):
    for j in range(c):
        if G[i][j] != 0 and not bridged[i][j]:
            build_bridge(i, j)

parent = [i for i in range(lv)] # lv == 섬의 개수

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    else:
        parent[b] = a
    return True

ans = 0
for i in range(len(bridges)):
    l, a, b = heappop(bridges)
    if union(a, b):
        ans += l

tmp = find(1)
flag = True
for i in range(2, len(parent)):
    if find(i) != tmp:
        flag = False
        
if flag:
    print(ans)
else:
    print(-1)
