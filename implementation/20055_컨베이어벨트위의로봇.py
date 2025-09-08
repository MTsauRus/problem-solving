### 20055 컨베이어 벨트 위의 로봇
### 구현, 시뮬레이션
import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())
hp = list(map(int, input().split()))
belt = [[i, h, False] for i, h in enumerate(hp)] # 자리번호, 내구도, 로봇점유여부
up = deque(belt[:N]) # 벨트의 윗부분
down = deque(belt[N:]) # 벨트의 아랫부분
robot_queue = deque() # 로봇이 들어온 순서
out_of_hp = 0 # hp가 0인 칸 수

def rotate():
    global up, down, robot_queue
    down.appendleft(up.pop())
    up.appendleft(down.pop())
    for i in range(len(robot_queue)):
        robot_queue[i] += 1
    if up[-1][2]: # 내리는 위치에 로봇이 있으면
        up[-1][2] = False
        robot_queue.popleft() # 로봇큐에서 삭제

    
def move():
    global up, down, robot_queue, out_of_hp
    is_deleted = False # 이동을 통해 로봇이 제거되었다면 True
    for i in range(len(robot_queue)):
        now_idx = robot_queue[i]
        if now_idx == N-1: # up의 오른쪽 끝자리라면 이동 불가
            continue
        if up[now_idx + 1][2]: # 다음 칸에 로봇이 있다면 이동 불가
            continue
        if up[now_idx + 1][1] == 0: # 다음 칸의 내구도가 0이면 이동 불가
            continue

        up[now_idx][2] = False # 현재 칸의 로봇을 제거
        up[now_idx+1][1] -= 1 # 다음 칸의 내구도 1 감소      
        up[now_idx+1][2] = True # 다음 칸으로 로봇을 이동
        robot_queue[i] += 1 # 로봇 큐에도 반영
        
        if now_idx+1 == N-1: #맨 끝자리로 이동했다면, 즉 제거되어야 한다면
            is_deleted = True
            up[now_idx+1][2] = False
        
        if up[now_idx+1][1] == 0: # 내구도가 0인 칸이 만들어지면 종료조건 + 1
            out_of_hp += 1
            
    if is_deleted:
        robot_queue.popleft()


def new_robot():
    global up, robot_queue, out_of_hp
    if up[0][1] > 0: # 내구도가 0이 아니라면 로봇을 올리자.
        robot_queue.append(0) # 현재 자리 번호, up 큐에서의 인덱스 번호
        up[0][2] = True
        up[0][1] -= 1
        if up[0][1] == 0:
            out_of_hp += 1


iter = 1
while out_of_hp < K:
    rotate()
    move()
    new_robot()
    
    iter += 1

print(iter-1)