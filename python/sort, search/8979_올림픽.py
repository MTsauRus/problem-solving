### 올림픽 (S5)
### 정렬
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
score = []
for i in range(a):
    tmp = list(map(int, input().split()))
    if tmp[0] == b:
        flag = tmp[1]*10**12 + tmp[2]*10**6 + tmp[3]
    score.append([tmp[0], tmp[1]*10**12 + tmp[2]*10**6 + tmp[3]])

cnt = 0
for i in score:
    if i[1] > flag:
        cnt += 1
print(cnt+1)


