### 14783 (S4)
### 구현, 자료구조
import sys

a, b = map(int, input().split())
L = list(map(int, input().split()))
N = [x for x in range(a)]

L_ptr = 0
N_ptr = 0

for i in range(a-1):
    # L 포인터 설정
    l = L[L_ptr]
    L_ptr += 1
    if L_ptr == len(L):
        L_ptr = 0
    
    # N 포인터 설정
    N_ptr = (N_ptr + l) % len(N)
    N.pop(N_ptr)
    
    # N 포인터 한 칸 뒤로 밀기
    N_ptr -= 1
    if N_ptr == -1:
        N_ptr = len(N)-1

print(N[0])