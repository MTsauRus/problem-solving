### 3190. 뱀 (G4)
### 시뮬레이션, 구현
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    r, c = map(int, input().split())
    apples.append([r-1, c-1])
moves = []
L = int(input())
for _ in range(L):
    sec, turn = input().split()
    sec = int(sec)
    moves.append([sec, turn])

moves.append([999, 'END']) # 임의의 마지막 이동 노드

moves = deque(moves)
G = [[-1 for _ in range(N)] for _ in range(N)]
G[0][0] = 0
## -1: 빈칸, -2: 사과, 0 이상: 뱀
for r, c in apples:
    G[r][c] = -2
    
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0] # -> ㅜ <- ㅗ
ans = 0
head = [0, 0]
tail = [0, 0]
next_node = [0, 1]
now_direction = 0
next_tmp = moves.popleft()
next_sec, next_turn = next_tmp[0], next_tmp[1]

def check_safe(next_node): # r, c는 다음 이동 칸
    r, c = next_node[0], next_node[1]
    
    # 칸을 벗어났거나, 뱀이라면
    if (not (0 <= r < N)) or (not (0 <= c < N)) or G[r][c] >= 0:
        return False # False: 종료
    return True
    
def sol():    
    global ans, head, tail, next_node, next_sec, next_turn, now_direction
    while True:
        if ans == next_sec: # 방향 전환 시기가 오면
            if next_turn == 'L':
                now_direction = (now_direction-1)%4
            else:
                now_direction = (now_direction+1)%4
            
            next_sec, next_turn = moves.popleft()
        
        next_node = [head[0] + dr[now_direction], head[1] + dc[now_direction]]    
        if not check_safe(next_node):
                return ans+1 # 게임 종료
            
        move()
        ans += 1
        #debug_print()
def move():
    global head, tail, next_node
    nr, nc = next_node[0], next_node[1] # 다음
    cr, cc = head[0], head[1] # 현재
    
    if G[nr][nc] == -2: # 다음칸이 사과라면
        G[nr][nc] = G[cr][cc] + 1 # 현재 노드 + 1을 다음 노드에 저장, 추후 모듈러 처리
        head = next_node # 다음 노드로 머리 이동
        return
    
    else: # 사과가 없었다면
        # 머리 이동은 동일
        G[nr][nc] = G[cr][cc] + 1 # 현재 노드 + 1을 다음 노드에 저장, 추후 모듈러 처리
        head = next_node # 다음 노드로 머리 이동
        tail_r, tail_c = tail[0], tail[1]
        for i in range(4):
            next_r = tail_r + dr[i]
            next_c = tail_c + dc[i]
            # 꼬리 바로 다음 칸을 찾으면
            if 0 <= next_r < N and 0 <= next_c < N and G[next_r][next_c] == G[tail_r][tail_c] + 1:
                G[tail_r][tail_c] = -1 # 원래 꼬리칸을 빈칸으로 만들고
                tail = [next_r, next_c] # 다음 칸을 꼬리로 업데이트
                break # 4짜리 for문에서 탈출

def debug_print():
    print(ans)
    for next in G:
        print(next)
    
    print()
    print()
        
#debug_print()
print(sol())