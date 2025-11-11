### 1011. Fly me to the Alpha Centauri (G5)
### 수학
### 
import sys
input = sys.stdin.readline
from math import sqrt

T = int(input())
for t in range(T):
    s, e = map(int, input().split())
    dist = e - s
    
    n = int(sqrt(dist))
    
    if n**2 == dist:
        print(2*n-1)
    elif n**2 < dist <= n**2+n:
        print(2*n)
    else:
        print(2*n+1)