import sys
input = sys.stdin.readline
from collections import deque

stack = deque()
def push(i):
    stack.append(i)

def pop():
    if not stack:
        return -1
    return stack.pop()

def size():
    return len(stack)

def empty():
    if stack:
        return 0
    return 1

def top():
    if stack:
        return stack[-1]

    return -1

N = int(input())
for _ in range(N):
    next = list(input().split())
    if next[0] == "push":
        push(int(next[1]))
    elif next[0] == "pop":
        print(pop())
    elif next[0] == "size":
        print(size())
    elif next[0] == "empty":
        print(empty())
    else:
        print(top())
    

