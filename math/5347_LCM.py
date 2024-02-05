### LCM (S5)
import sys
import math
input = sys.stdin.readline

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
    