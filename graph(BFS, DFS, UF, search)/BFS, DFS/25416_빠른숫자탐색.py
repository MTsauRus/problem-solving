### 빠른 숫자 탐색 (S2)
import sys
from collections import deque
input = sys.stdin.readline

G = []
for _ in range(5):
    G.append(list(map(int, input().split())))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
r, c = map(int, input().split())
Q = deque()
Q.append([r, c])
while Q:
    nowr, nowc = Q.popleft()
    #G[nowr][nowc] = -1
    for i in range(4):
        nextr = nowr + dr[i]
        nextc = nowc + dc[i]
        if 0 <= nextr < 5 and 0 <= nextc < 5:
            if G[nextr][nextc] == 1:
                print((G[nowr][nowc] + 2)//2) 
                exit(0) 
            elif G[nextr][nextc] == 0:
                G[nextr][nextc] = G[nowr][nowc] + 2 #2씩 더해야 위치 1과 겹치지 않음
                Q.append([nextr, nextc])
print(-1)