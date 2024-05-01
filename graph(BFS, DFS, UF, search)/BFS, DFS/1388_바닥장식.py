### 바닥 장식 (S4)
import sys
input = sys.stdin.readline
from collections import deque

row, col = map(int, input().split())
tile = []
for i in range(row):
    tile.append(list(input().strip()))
visited = [[False for _ in range(col)] for _ in range(row)]

ans = 0
flag = False
for r in range(row):
    for c in range(col):
        if flag and tile[r][c] == '-':
            continue
        elif not flag and tile[r][c] == '-':
            flag = True
            ans += 1
        else:
            flag = False
    flag = False
    
flag = False
for c in range(col):
    for r in range(row):
        if flag and tile[r][c] == '|':
            continue
        elif not flag and tile[r][c] == '|':
            flag = True
            ans += 1
        else:
            flag = False
    flag = False

print(ans)