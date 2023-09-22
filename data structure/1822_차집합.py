### 차집합(S4) 
import sys
input = sys.stdin.readline

A = set()
B = set()
_, _ = map(int, input().split())
tmp = list(map(int, input().split()))
A.update(tmp)
tmp = list(map(int, input().split()))
B.update(tmp)
A.difference_update(B)
if len(A) == 0:
    print(0)
else:
    print(len(A))
    A = sorted(list(A))
    print(*A)