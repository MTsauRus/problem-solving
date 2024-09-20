"""
계단 오르기 (S3)
DP
"""
import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n):
    score.append(int(input()))

if n == 1:
    print(score[0])
    exit(0)
if n == 2:
    print(sum(score))
    exit(0)

D = [0 for i in range(n+2)]
D[0] = score[0]
D[1] = score[0] + score[1]
D[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, n):
    D[i] = max(D[i-2]+score[i], D[i-3]+score[i-1]+score[i])

print(D[n-1])