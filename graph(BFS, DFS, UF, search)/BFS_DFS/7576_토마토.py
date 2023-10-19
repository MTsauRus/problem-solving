### 토마토 (G5)
import sys
input = sys.stdin.readline
from collections import deque

C, R = map(int, input().split())
box = []
tomato = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt_zero = 0
cnt_one = 0
cnt_minus = 0

for _ in range(R):
    box.append(list(map(int, input().split())))
for r in range(R):
    for c in range(C):
        if box[r][c] == 1:
           tomato.append([r, c])
           cnt_one += 1
        elif box[r][c] == 0:
            cnt_zero += 1
        else:
            cnt_minus += 1

if cnt_minus + cnt_one == C*R: # 박스에 안익은 토마토가 없는 경우
    print(0)
    exit(0)
           
tomatoes = len(tomato)
queueSet = [deque()] * tomatoes

global ans
ans = 0

def bfs(queueNum):
    global ans
    if not queueSet[queueNum]:
        return False
    x, y = queueSet[queueNum].popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < R and 0 <= ny < C:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                if box[nx][ny] > ans:
                    ans = box[nx][ny]
                    
                queueSet[queueNum].append([nx, ny])
    return True

for i in range(tomatoes):
    queueSet[i].append(tomato[i])

while True:
    cnt = 0
    for i in range(tomatoes):
        if not bfs(i):
            cnt += 1
    if cnt == tomatoes:
        break

for r in range(R):
    for c in range(C):
        if box[r][c] == 0: # bfs 후 안익은 토마토가 있는 경우
            print(-1)
            exit(0)

print(ans-1)
        
    
        