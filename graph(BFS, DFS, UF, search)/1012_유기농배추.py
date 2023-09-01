### 유기농 배추 (S2)
import sys
input = sys.stdin.readline

N = int(input())

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = []
    queue.append((x, y))
    yard[x][y] = 0
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < row and 0 <= ny and ny < col:
                if yard[nx][ny] == 1:
                    yard[nx][ny] = 0
                    queue.append((nx, ny))


for n in range(N):
    ans = 0
    row, col, cabbage = map(int, input().split())
    yard = [[0 for c in range(col)] for r in range(row)]
    for i in range(cabbage):
        x, y = map(int, input().split())
        yard[x][y] = 1
    
    for r in range(row):
        for c in range(col):
            if yard[r][c] == 1:
                bfs(r, c)
                ans += 1
                
    print(ans)
                
            
        