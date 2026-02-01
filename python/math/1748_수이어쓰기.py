### 수 이어쓰기 (S4)
import sys
input = sys.stdin.readline

N = input().strip()
l = len(N)
if 1 <= int(N) <= 9:
    print(int(N))
    exit(0)
ans = 0
N = int(N)
tmp = 9
for i in range(1, l):
    ans += i * tmp
    tmp *= 10

N -= 10**(l-1)
N += 1
ans += N * l
print(ans)