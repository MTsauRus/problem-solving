### 폴짝폴짝 (S2)
import sys
from collections import deque
N = int(input())
bridge = [0]
bridge += (list(map(int, input().split())))
start, end = map(int, input().split())

def bfs(start, end):
    if start == end:
        return 0
    
    queue = deque()
    queue.append([start, 0])
    while queue:
        now, cnt = queue.popleft()
        mul = bridge[now]
        
        if now == end:
            return cnt
        
        minus_flag = True
        plus_flag = True
        num = 1
        while True:
            next = mul * num
            if not (0 < now - next <= N):
                minus_flag = False
            if not (0 < now + next <= N):
                plus_flag = False
            
            if minus_flag:
                queue.append([now - next, cnt + 1])
            if plus_flag:
                queue.append([now + next, cnt + 1])
            if not minus_flag and not plus_flag:
                break
            num += 1
            
    return -1

            

print(bfs(start, end))