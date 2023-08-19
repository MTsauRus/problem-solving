### 2xn 타일링 (S3)
import sys
from math import factorial
input = sys.stdin.readline

n = int(input())
mod = 10007
ans = 0
one = 0 # 1의 개수
two = 0 # 2의 개수
for i in range(n // 2 + 1):
    one = n - (2 * i) # 1의 개수
    two = i # 2의 개수
    ans += factorial(n-i) // (factorial(one) * factorial(two))

print(ans % mod)
