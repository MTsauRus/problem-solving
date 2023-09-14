### 숨바꼭질2 (G4)
import sys
from collections import deque
A, goal = map(int, input().split())

def bfs(start):
    sec = [0 for i in range(100001)]
    tmp = [0, 0, 0]
    cnt = 0
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now == goal:
            return sec[now], cnt
        
        else:
            tmp[0], tmp[1], tmp[2] = now-1, now+1, now*2
            for next in tmp:
                if next >= 0 and next <= 100000:
                    cnt += 1 ## ans까지 도달했을 때의 next 개수
                    if sec[next] == 0:
                        sec[next] = sec[now] + 1
                        queue.append(next)

ans, cnt = bfs(A)
def bfs2(start, cnt):
    sec = [0 for i in range(100001)]
    tmp = [0, 0, 0]
    secondAns = 0
    queue = deque()
    queue.append(start)
    for i in range(cnt+5):
        now = queue.popleft()
        if now == goal:
            secondAns += 1
        tmp[0], tmp[1], tmp[2] = now-1, now+1, now*2
        for next in tmp:
            if next >= 0 and next <= 100000:
                sec[next] = sec[now] + 1
                queue.append(next)
    print(sec[:20])
    return secondAns
ans2 = bfs2(A, cnt)
print(ans)
print(ans2)
