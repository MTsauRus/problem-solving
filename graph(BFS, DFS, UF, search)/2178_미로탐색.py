### 미로 탐색 (S1)
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
maze = [[0 for c in range(col)] for r in range(row)]
for i in range(row):
    next = input().strip()
    for j in range(col):
        maze[i][j] = int(next[j])

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = []
    queue.append((x, y))
    
    while queue:
        now = queue.pop(0)
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            
            if 0 <= nx and nx < row and 0 <= ny and ny < col:
                if maze[nx][ny] == 1:
                    queue.append((nx, ny))
                    maze[nx][ny] += maze[now[0]][now[1]]
                
bfs(0, 0)    
print(maze[row-1][col-1])
                
                
            

    
    
    




### 예전 풀이

# import sys
# input = sys.stdin.readline

# row, col = map(int, input().split())
# maze = [[0 for c in range(col)] for r in range(row)]
# visited = [[False for c in range(col)] for r in range(row)]

# for i in range(row):
#     numbers = list(input().strip())
#     for j in range(col):
#         maze[i][j] = int(numbers[j])

# def check(a, b):
#     return 0 <= a and a < row and 0 <= b and b < col

# def make_around(a, b):
#     l = []
#     l.append((a-1, b)) # up
#     l.append((a+1, b)) # down
#     l.append((a, b-1)) # left
#     l.append((a, b+1)) # right
#     return l

# def BFS(a, b):
#     queue = []
#     queue.append((a,b))
#     visited[a][b] = True
#     while queue:
#         now = queue.pop(0)
#         around = make_around(now[0], now[1])

#         for a in around:
#             if check(a[0], a[1]) and not visited[a[0]][a[1]] and maze[a[0]][a[1]] > 0:
#                 queue.append(a)
#                 visited[a[0]][a[1]] = True
#                 maze[a[0]][a[1]] = maze[now[0]][now[1]] + 1

# BFS(0, 0)
# print(maze[-1][-1])



