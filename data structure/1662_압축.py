### 압축 (G5)
### 재귀, 스택
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

L = list(input().strip())
global ans
ans = 0

def recur(l):
    global ans
    Q = ""
    K = 0
    for i in range(len(l)):
        if l[i] == '(':
            ans += recur(l[i+1:])
        
        if l[i] == ')':
            Q = l[left:i]
            K = int(l[left-1])
            return K * len(Q)
    return len(l)

recur(L, 0)
print(ans)    