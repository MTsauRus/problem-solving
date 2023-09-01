### Z (S1)
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
ans = []
for i in range(N, 0, -1):
    mid = 2**(i-1) - 1
    if 0 <= r and r <= mid:
        if 0 <= c and c <= mid:
            ans.append(0)
        else:
            c %= 2**(i-1)
            ans.append(1)
    else:
        r %= 2**(i-1)
        if 0 <= c and c <= mid:
            ans.append(2)
        else:
            c %= 2**(i-1)
            ans.append(3)


mult = (2**(N-1)) ** 2

res = 0

for next in ans:
    res += next * mult
    mult //= 4

print(res)
