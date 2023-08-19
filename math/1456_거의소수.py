import sys
from collections import deque
input = sys.stdin.readline

def seive(a, b): 
    l = [False, False] + [True] * int(b**0.5 + 1)
    
    for i in range(2, int(b**0.5 + 1)):
        if l[i] == True:
            for j in range(i * 2, int(b**0.5 + 1), i):
                l[j] = False
    ### 소수 구하기 끝
    prime = [i for i in range(int(b**0.5 + 1)) if l[i] == True]
    
    ans = 0
    for p in prime:
        now = p**2
        while now <= b:
            if now >= a:
                ans += 1
            now *= p
    
    return ans


a, b = map(int, input().split())
print(seive(a, b))

