### 트리 순회(S1)
import sys
input = sys.stdin.readline

T = dict()
N = int(input())

for i in range(N):
    root, l, r = input().split()
    T[root] = [l, r]

def pre_order(a):
    now = a
    if now == '.':
        return
    
    print(now, end="")
    pre_order(T[now][0])
    pre_order(T[now][1])

def in_order(a):
    now = a
    if now == '.':
        return
    
    in_order(T[now][0])
    print(now, end="")
    in_order(T[now][1])    

def post_order(a):
    now = a
    if now == '.':
        return
    
    post_order(T[now][0])
    post_order(T[now][1])    
    print(now, end="")

pre_order('A')
print()
in_order('A')
print()
post_order('A')