### 10942.팰린드롬? (G4)
### 구현, 재귀, DP?
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
D = [[False for _ in range(N)] for _ in range(N)]

for i in range(N): # 길이 1
    D[i][i] = True
for i in range(N-1): # 길이 2
    if nums[i] == nums[i+1]:
        D[i][i+1] = True
for length in range(3, N+1):
    for s in range(0, N-length+1): 
        e = s + length - 1
        if nums[s] != nums[e]:
            D[s][e] = False
        else:
            D[s][e] = D[s+1][e-1]
            
Q = int(input())
for _ in range(Q):
    s, e = map(int, input().split())
    print(int(D[s-1][e-1]))