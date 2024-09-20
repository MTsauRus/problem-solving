"""
마라톤 16
알고리즘 수업 - 피보나치 수 2 (S4)
DP, 수학
"""
import sys
input = sys.stdin.readline
mod = 1000000007
n = int(input())

a = 1
b = 1
for i in range(2, n):
    c = (a + b)%mod
    a = b
    b = c
print(c%mod, (n-2)%mod)

