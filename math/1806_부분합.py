### 부분합 (G4)
import sys
input = sys.stdin.readline

N, key = map(int, input().split())
S = [0] + list(map(int, input().split()))
ans = N+2
tmp = 0
for i in range(1, N+1):
    S[i] = S[i-1] + S[i]

l, r = 0, 1 # ptr
while True:
    if r >= N+1:
        break
    tmpA = r - l
    tmpS = S[r] - S[l]
    if tmpS < key:
        if r < N:
            r += 1
        else:
            break
    
    else: # 구간 합이 key보다 클 때
        if tmpA < ans:
            ans = tmpA
        if tmpA > 1: # 두 칸 이상 떨어져 있다면
            l += 1
        else:
            if r < N:
                r += 1
                l += 1
            else:
                break
if ans == N+2:
    print(0)
else:
    print(ans)
