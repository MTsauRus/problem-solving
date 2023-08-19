### 제곱ㄴㄴ수 (G1)
import sys
input = sys.stdin.readline

min, max = map(int, input().split())
num = [1] * (max - min + 1)
start = 0

for i in range(2, int(max ** 0.5) + 1):
    square = i * i
    if min % square == 0:
        start = 0
    else:
        start = square - (min % square)
    for j in range(start, len(num), square):
        if num[j] == 1:
            num[j] = 0

print(sum(num))


