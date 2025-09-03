### 빗물 (G5)
### 구현
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int ,input().split())
block = list(map(int, input().split()))
G = [[0 for _ in range(W)] for _ in range(H)]

front_queue = deque()
back_queue = deque()
ans = 0
for i in range(W):
    for j in range(block[i]):
        G[j][i] = -1
        front_queue.append([j, i])
        back_queue.append([j, i])
        
while front_queue:
    x, y = front_queue.popleft()
    if y+1 < W and G[x][y+1] == 0:
        G[x][y+1] = 1
        front_queue.append([x, y+1])

while back_queue:
    x, y = back_queue.pop()
    if 0 <= y-1 and G[x][y-1] == 1:
        G[x][y-1] = 2
        ans += 1
        back_queue.append([x, y-1])

print(ans)