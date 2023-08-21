### 괄호 (S4)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    stack = deque()
    PS = input().strip()
    for next in PS:
        if next == "(":
            stack.append(next)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(-1)
                break
            
    if stack:
        print("NO")
    else:
        print("YES")
