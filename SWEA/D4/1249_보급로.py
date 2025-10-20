### 1249. 보급로 (D4)
from heapq import heappop, heappush
T = int(input())
for i in range(1, T+1):
    n = int(input())
    G = [list(map(int, input().strip())) for _ in range(n)]
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    #visited = [[False for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = [[0, 0, 0]] # weight, x, y
    while queue:
        now_dist, x, y = heappop(queue)
        if now_dist > dist[x][y]: # 새로 꺼낸 거리 > 기존 거리면 무의미	
            continue
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < n:
                next_dist = now_dist + G[nx][ny] # 지금까지 거리 + 새로 꺼낸 weight
                if dist[nx][ny] > next_dist:
                    dist[nx][ny] = next_dist
                    #visited[nx][ny] = True
                    heappush(queue, [next_dist, nx, ny])
    print(f'#{i} {dist[n-1][n-1]}')
