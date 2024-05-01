### 뱀과 사다리 게임 (G5)
### bfs
import sys
input = sys.stdin.readline
from collections import deque

board = [i for i in range(0, 106)]
dist = [0 for i in range(0, 106)]
a, b = map(int, input().split())
for i in range(a+b):
    c, d = map(int, input().split())
    board[c] = d

Q = deque()
Q.append(1)
dist[1] = 1
while Q:
    now = Q.popleft()
    if now == 100: # 종료 조건
        print(dist[now] - 1)
        break
    
    for i in range(now + 1, now + 7):
        next = board[i]
        if dist[next] == 0: # not visited
            dist[next] = dist[now] + 1
            Q.append(next)
            
