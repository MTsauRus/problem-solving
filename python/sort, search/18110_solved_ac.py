import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
    exit(0)
cut = round(N * 0.15 + 0.0000001)
score = []
for _ in range(N):
    score.append(int(input()))
    
score.sort()
score = score[cut:N-cut]
print(round((sum(score) / (N - cut*2)) + 0.0000001))

