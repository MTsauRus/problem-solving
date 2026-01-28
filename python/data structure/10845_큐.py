import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input())
for _ in range(N):
    next = list(input().split())
    if next[0] == "push":
        queue.append(next[1])
    elif next[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif next[0] == "size":
        print(len(queue))
    elif next[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif next[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])

        
    