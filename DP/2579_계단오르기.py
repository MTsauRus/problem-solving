### 계단 오르기 (S3)
import sys
input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

if N == 1:
    print(score[0])
    exit(0)
if N == 2:
    print(score[0]+score[1])
    exit(0)

D = [0] * N
D[0] = score[0]
D[1] = score[0]+score[1]
D[2] = max(score[0]+score[2], score[1]+score[2])

for i in range(2, N):
    D[i] = max(score[i] + D[i-2], score[i] + score[i-1] + D[i-3])

print(D[N-1])
