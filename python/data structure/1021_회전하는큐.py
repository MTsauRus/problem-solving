### 회전하는 큐 (S3)
import sys
from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))
want = list(map(int, input().split()))
cnt = 0

for next in want:
    dis = 0
    if next == queue[0]:
        queue.popleft()
        n -= 1
        continue

    while queue[0] != next:
        queue.append(queue.popleft())
        dis += 1
    
    if dis <= len(queue) // 2:
        cnt += dis
    else:
        cnt += len(queue) - dis
        
    queue.popleft()
    
print(cnt)

