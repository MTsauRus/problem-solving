### 2531 회전 초밥 (S1)
### 자료구조, 덱

import sys
input = sys.stdin.readline
from collections import deque

N, sushi, k, event = map(int, input().split())
belt = []
for _ in range(N):
    belt.append(int(input()))

ans = 0
eat = deque(belt[:k])
eat_set = set()
eat_set.update(list(eat))
ans = len(eat_set)

for i in range(k, N+k):
    eat.popleft()
    eat.append(belt[i%N])
    eat_set = set(eat)
    if event not in eat_set:
        eat_set.add(event)
    
    if len(eat_set) > ans:
        ans = len(eat_set)

print(ans)