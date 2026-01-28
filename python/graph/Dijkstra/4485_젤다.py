### 4485 녹색 옷 입은 애가 젤다지? (G4)
### 그래프 탐색, 다익스트라
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
iter = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    G = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    queue = [[G[0][0], 0, 0]] # dist, x, y
    dist[0][0] = G[0][0]
    
    while queue:
        now_dist, x, y = heappop(queue)
        if dist[x][y] < now_dist: # 새로 꺼낸게 현재까지의 거리보다 큰 경우 무의미
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                next_dist = now_dist + G[nx][ny]
                if dist[nx][ny] > next_dist:
                    dist[nx][ny] = next_dist
                    heappush(queue, [next_dist, nx, ny])
                    
    print(f"Problem {iter}: {dist[N-1][N-1]}")
    iter += 1