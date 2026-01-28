### 나이트의 이동 (S1)
### bfs
from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
N=int(input())
for _ in range(N):
    l = int(input())
    s = list(map(int, input().split()))
    g = list(map(int, input().split()))
    
    if s == g: # 시작점이 목적지와 같은 경우
        print(0)
        continue
    
    ans_flag = False
    Q = deque()
    Q.append(s)
    
    board = [[0 for _ in range(l)] for _ in range(l)]
    while Q:
        nowx, nowy = Q.popleft()
        if ans_flag == True:
            break
        for i in range(8):
            nextx = nowx+dx[i]
            nexty = nowy+dy[i]
            if nextx == g[0] and nexty == g[1]:
                print(board[nowx][nowy] + 1)
                ans_flag = True
                break
            
            if (0 <= nextx and nextx < l) and (0 <= nexty and nexty < l):
                if board[nextx][nexty] == 0: # not visited
                    board[nextx][nexty] = board[nowx][nowy] + 1
                    Q.append([nextx, nexty])