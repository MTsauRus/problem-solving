### 16234 인구 이동
### bfs
import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
G = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    G.append(list(map(int, input().split())))
        
def bfs(lv, s, e):
    if visited[s][e] == lv: # 이미 방문
        return
    visited[s][e] += 1 # 방문처리
    
    queue = deque([[s, e]])
    union = [[s, e]]
    population = G[s][e] # 유니온 인구 수
    is_moved = False # 인구 이동이 한 번이라도 일어났다면 True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == lv-1: # lv: 현재 시행 횟수. lv-1: 방문하지 않음
                if L <= abs(G[x][y] - G[nx][ny]) <= R: # 인구수 조건을 만족한다면
                    is_moved = True
                    queue.append([nx, ny])
                    union.append([nx, ny]) # 같은 연합임
                    population += G[nx][ny]
                    visited[nx][ny] += 1
                    
    avg_population = population // len(union)

    for x, y in union:
        G[x][y] = avg_population
        
    return is_moved
    
iter = 1
is_moved_all = False
is_moved_union = False
while True:
    for i in range(N):
        for j in range(N):
            is_moved_union = bfs(iter, i, j)
            if is_moved_union:
                is_moved_all = True
                
    if not is_moved_all:
        print(iter-1)
        break
    is_moved_union = False
    is_moved_all = False
    iter += 1