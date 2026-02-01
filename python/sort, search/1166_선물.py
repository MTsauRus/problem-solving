### 선물 (S3)
import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())
start = 0
end = min(L, W, H)
for i in range(10000):
    a = (start + end) / 2
    tmp = (L//a) * (W//a) * (H//a)
    if tmp >= N:
        start = a
    else:
        end = a
print("%.10f" %(a))