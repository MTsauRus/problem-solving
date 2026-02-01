### 1309. 동물원
### 
import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    D = [0 for _ in range(N+1)]
    D[2] = 2
    for i in range(3, N+1):
        D[i] = D[i-1] + 2*((i-1)**2)

    print(D[N] + N*2 + 1)