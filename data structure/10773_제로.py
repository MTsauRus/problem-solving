import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
stack = deque()

for _ in range(N):
    next = int(input())
    if next != 0:
        stack.append(next)
        continue
    stack.pop()
    
print(sum(stack))