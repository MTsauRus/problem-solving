### 2961 도영이가 만든 맛있는 음식 (S2)
### 구현, 비트마스킹
import sys
input = sys.stdin.readline

N = int(input())
foods = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(1, 1 << N):
    S, B = 1, 0
    
    for j in range(N):
        if i & (1 << j): # j번째 비트가 1일 때 j번째 음식을 사용해서 계산
            S *= foods[j][0]
            B += foods[j][1]
    if ans > abs(S-B):
        ans = abs(S-B)

print(ans)