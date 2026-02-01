### 균형잡힌 세상 (S4)
import sys
input = sys.stdin.readline
from collections import deque

while True:
    next = input()
    if next == '.\n':
        break
    queue = deque()
    for ch in next:
        if ch in ['(', ')', '[', ']']:
            if queue:
                if queue[-1] == '(':
                    if ch == ')':
                        queue.pop()
                        continue
                    else:
                        queue.append(ch)
                
                elif queue[-1] == '[':
                    if ch == ']':
                        queue.pop()
                        continue
                    else:
                        queue.append(ch)
                
            else:
                queue.append(ch)
    if queue:
        print('no')
    else:
        print('yes')
                
