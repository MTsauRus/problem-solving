"""
1로 만들기 (S3)
DP
bottom up 방식
"""
import sys
input = sys.stdin.readline

a = int(input())
D = [0 for i in range(a+1)]

for i in range(2, a+1):
    D[i] = D[i-1] + 1
    if i % 2 == 0: # 2로 나누어 떨어지면 D[i//2]와 비교
        D[i] = min(D[i//2]+1, D[i])
    if i % 3 == 0: 
        D[i] = min(D[i//3] + 1, D[i])

print(D[a])