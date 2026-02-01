### A -> B (S2)
### BFS (그리디로도 가능)

import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append([a, 0])
    
    while q:
        c, d = q.popleft()
        if c == b:
            return d + 1
        if c < b:
            q.append([c*2, d+1])
            q.append([c*10+1, d+1])
        
    return -1

a, b = map(int, input().split())
print(bfs(a, b))