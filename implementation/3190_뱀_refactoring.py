### 3190. 뱀 (G4) - 리팩토링
### 시뮬레이션, 구현
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2 # 사과: 2
    
L = int(input())
turns = {} # 방향 정보 -> dict
for _ in range(L):
    x, c = input().split()
    turns[int(x)] = c
    
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def sol():
    x, y = 0, 0 # 현재 뱀의 머리
    board[0][0] = 1 # 현재 뱀의 몸통 표시
    direction = 0 # 초기 방향 ->
    time = 0 # 현재 경과 시간
    
    snake = deque([(0, 0)]) 
    
    while True:
        time += 1
        
        nx = x + dr[direction]
        ny = y + dc[direction]
        
        # 다음 방향이 벽이거나 자기 몸일 때
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1:
            return time
        
        # 이동
        if board[nx][ny] == 2: # 사과가 있다면
            board[nx][ny] = 1 # 머리 이동
            snake.append((nx, ny)) # 뱀에 새 머리 append.
        else: # 사과가 없다면
            board[nx][ny] = 1 # 머리 이동
            snake.append((nx, ny)) # 뱀에 새 머리 append. 여기까지 같음.
            
            tx, ty = snake.popleft() # 꼬리 제거
            board[tx][ty] = 0 # 보드에서 꼬리 제거
            
        x, y = nx, ny # 머리 갱신
        
        if time in turns: # 현재 시간이 turns의 key에 있다면
            if turns[time] == 'D':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
                
print(sol())