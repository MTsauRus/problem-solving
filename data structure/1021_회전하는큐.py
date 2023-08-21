### 회전하는 큐 (S3)
import sys
from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n+1))
want = list(map(int, input().split()))
cnt = 0

for next in want:
    if next == queue[0]:
        queue.popleft()
        n -= 1
        print(queue, cnt)
        continue

    dis = 
    if dis <= n // 2 + 1:
        while queue[0] != next:
            queue.append(queue.popleft())
            cnt += 1
        queue.popleft()
    else:
        while queue[0] != next:
            queue.appendleft(queue.pop())
            cnt += 1
        queue.popleft()
    print(queue, cnt)
    n -= 1
        
print(cnt)

