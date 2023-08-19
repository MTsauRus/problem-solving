import sys
input = sys.stdin.readline

row, col = map(int, input().split())
maze = [[0 for c in range(col)] for r in range(row)]
visited = [[False for c in range(col)] for r in range(row)]

for i in range(row):
    numbers = list(input().strip())
    for j in range(col):
        maze[i][j] = int(numbers[j])

def check(a, b):
    return 0 <= a and a < row and 0 <= b and b < col

def make_around(a, b):
    l = []
    l.append((a-1, b)) # up
    l.append((a+1, b)) # down
    l.append((a, b-1)) # left
    l.append((a, b+1)) # right
    return l

def BFS(a, b):
    queue = []
    queue.append((a,b))
    visited[a][b] = True
    while queue:
        now = queue.pop(0)
        around = make_around(now[0], now[1])

        for a in around:
            if check(a[0], a[1]) and not visited[a[0]][a[1]] and maze[a[0]][a[1]] > 0:
                queue.append(a)
                visited[a[0]][a[1]] = True
                maze[a[0]][a[1]] = maze[now[0]][now[1]] + 1

BFS(0, 0)
print(maze[-1][-1])













# def BFS(a, b):
#     queue = []
#     queue.append((a, b))

#     while queue:
#         now = queue.pop(0)
#         visited[now[0]][now[1]] = True
#         up = (now[0]-1, now[1])
#         down = (now[0]+1, now[1])
#         left = (now[0], now[1]-1)
#         right = (now[0], now[1]+1)
#         around = [up, down, left, right]
#         for node in around:
#             if 0 <= node[0] and node[0] < row and 0 <= node[1] and node[1] < col:
#                 if not visited[node[0]][node[1]] and maze[node[0]][node[1]] != 0:
#                     queue.append(node)
#                     maze[node[0]][node[1]] = maze[now[0]][now[1]] + 1
# BFS(0, 0)
# print(maze[-1][-1])



