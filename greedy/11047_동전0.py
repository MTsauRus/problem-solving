### 동전0 (S4)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
moneys = []
for _ in range(N):
    moneys.append(int(input()))

cnt = 0
pnt = len(moneys) - 1

while K != 0:
    while K - moneys[pnt] >= 0:
        tmp = K//moneys[pnt]
        K -= moneys[pnt] * tmp
        cnt += tmp
        # K -= moneys[pnt]
        # cnt += 1
    pnt -= 1

print(cnt)