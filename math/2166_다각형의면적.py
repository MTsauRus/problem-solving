### 2166 다각형의 면적 (G5)
### 수학
import sys
input = sys.stdin.readline

N = int(input())
V = []
for _ in range(N):
    V.append(list(map(int, input().split())))
V.append(V[0])
x, y = 0.0, 0.0
for i in range(N):
    x += V[i][0] * V[i+1][1]
    y += V[i][1] * V[i+1][0]

ans = round(0.5 * abs(x-y), 2)
print(ans)