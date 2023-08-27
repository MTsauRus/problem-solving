import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
for _ in range(N):
    n, ptr = map(int, input().split())
    
    l = list(map(int, input().split()))
    prior = sorted(l)
    l = deque(map(lambda x : [x, False], l))
    l[ptr][1] = True
    
    max = prior.pop()
    cnt = 0
    while l:
        if l[0][0] < max:
            l.append(l.popleft())
            
        else:
            now = l.popleft()
            cnt += 1
            if now[1] == True:
                print(cnt)
                break
            max = prior.pop()