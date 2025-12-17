### 1600. 말이 되고픈 원숭이 (G3)
### BFS
import sys
input = sys.stdin.readline
from collections import deque
K = int(input())
C, R = map(int, input().split())
G = []
for _ in range(R):
    G.append(list(map(int, input().split())))

# 0~3: 기본이동, 4~ 말 이동
dr = [1, -1, 0, 0, -2, -1, 1, 2, 2, 1, -1, -2]
dc = [0, 0, 1, -1, 1, 2, 2, 1, -1, -2, -2, -1]
visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(K+1)]
ans = -1
queue = deque()
queue.append([0, 0, 0, 0]) # k, r, c, iter
visited[0][0][0] = True
while queue:
    k, r, c, iter = queue.popleft()
    if r == R-1 and c == C-1:
        ans = iter
        break
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != 1 and not visited[k][nr][nc]:
            visited[k][nr][nc] = True
            queue.append([k, nr, nc, iter+1])


    if k < K: # 말 이동 방식 유효한 경우
        for i in range(4, 12):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != 1 and not visited[k+1][nr][nc]:
                visited[k+1][nr][nc] = True # 말 이동 방문체크
                queue.append([k+1, nr, nc, iter+1])    

print(ans)