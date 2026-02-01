### 숨바꼭질2 (G4)
import sys
from collections import deque
A, goal = map(int, input().split())

def bfs(start):
    sec = [0 for i in range(100001)]
    tmp = [0, 0, 0]
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now == goal:
            
            print(sec[:20])
            return sec[now]
        
        else:
            tmp[0], tmp[1], tmp[2] = now-1, now+1, now*2
            for next in tmp:
                if next >= 0 and next <= 100000:
                    if sec[next] == 0:
                        sec[next] = sec[now] + 1
                        queue.append(next)


print(bfs(A))
