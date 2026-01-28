### 최대공약수(S1)
import sys
input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

a, b = map(int, input().split())

for _ in range(GCD(a, b)):
    print(1, end="")
