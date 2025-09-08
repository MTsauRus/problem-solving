### 아기 상어 (G3)
### 1. dx, dy 순서는 queue 접근 우선순위에 영향을 주지 않음 -> sort해야 함.
### 2. 이 문제 핵심은 dist, x, y를 오름차순으로 sort하여 다음 노드 순서를 정하는 것

import sys
input = sys.stdin.readline

N = int(input())
G = []
visited = [[0 for _ in range(N)] for _ in range(N)]

cnt = [0] * 30 # 상어는 대략 30보다 커질 수 없음
status = (2, 0) # 크기, 먹은 물고기 수
ans = 0
for _ in range(N):
    G.append(list(map(int, input().split())))
start = [0, 0, 0] # dist, x, y
for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            start = [0, i, j]
            G[i][j] = 0
        else:
            cnt[G[i][j]] += 1
            
# def check():
#     global status, cnt, ans
#     lv = status[0] # 현재 레벨
#     for i in range(1, lv):
#         if cnt[i] != 0:
#             return False
#     return True

def eat(status):
    global visited
    lv, eaten = status[0], status[1]
    eaten += 1
    if lv == eaten:
        lv += 1
        eaten = 0
    
    visited = [[0 for _ in range(N)] for _ in range(N)] # visited 초기화
    
    return (lv, eaten)

def sol(x, y):
    global cnt, status, visited, ans 
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    queue = []
    queue.append(start)
    
    while queue:
        #if check(): break # 종료조건 검사

        queue.sort() ### 거리, x, y 오름차순으로 정렬
        _, x, y = queue.pop(0)
        if G[x][y] < status[0] and G[x][y] != 0: # 현재 칸 물고기를 먹을 수 있을 때
            cnt[G[x][y]] -= 1
            # print("now: ", x, y, "status: ", status, "eat: ", G[x][y], "ans: ", ans)
            G[x][y] = 0
            ans += visited[x][y] # 이동거리 추가
            status = eat(status) # 물고기를 먹고 현재 레벨 반영
            queue.clear() # 큐 초기화
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if G[nx][ny] <= status[0] and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1 # visited: 0이 아닌 수. 거리를 의미함
                    queue.append((visited[nx][ny], nx, ny))
                    
sol(start[0], start[1])
print(ans)

