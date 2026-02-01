# ### 소수 구하기(S3)
import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

def prime(a, b): 
    l = [False, False] + [True] * (b - 1)
    for i in range(2, int(b**0.5 + 1)):
        if l[i] == True:
            for j in range(i * 2, b + 1, i):
                l[j] = False
                
    return [i for i in range(a, b+1) if l[i] == True]

l = prime(a, b)
for i in l:
    print(i)
        