### 14783 (S4)
### 구현, 자료구조
### 다른 풀이: popleft()를 append함으로써 원형큐 구현
import sys
from collections import deque

n, l = map(int, input().split())
L = list(map(int, input().split()))
N = deque(x for x in range(n))
i = 0

for _ in range(n-1):
    for __ in range(L[i%l]-1):
        N.append(N.popleft())
    N.popleft()
    i+=1

print(N.pop()+1)


