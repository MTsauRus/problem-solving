### 토마토 3D.ver (G5)
import sys
input = sys.stdin.readline
from collections import deque

C, R, H = map(int, input().split())
box = [[] for _ in range(H)]
tomato = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

cnt_zero = 0
cnt_one = 0
cnt_minus = 0

for h in range(H):
    for _ in range(R):
        box[h].append(list(map(int, input().split())))
        
for h in range(H):
    for r in range(R):
        for c in range(C):
            if box[h][r][c] == 1:
                tomato.append([h, r, c])
                cnt_one += 1
            elif box[h][r][c] == 0:
                cnt_zero += 1
            else:
                cnt_minus += 1

if cnt_minus + cnt_one == H*C*R: # 박스에 안익은 토마토가 없는 경우
    print(0)
    exit(0)
           
tomatoes = len(tomato)

global ans
ans = 0

def bfs():
    global ans
    while tomato:
        z, x, y = tomato.popleft()
        for i in range(6):
            nz = dz[i] + z
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < H:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    if box[nz][nx][ny] > ans:
                        ans = box[nz][nx][ny]
                        
                    tomato.append([nz, nx, ny])
bfs()

for h in range(H):
    for r in range(R):
        for c in range(C):
            if box[h][r][c] == 0: # bfs 후 안익은 토마토가 있는 경우
                print(-1)
                exit(0)

print(ans-1)
