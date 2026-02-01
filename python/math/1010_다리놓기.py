### 다리 놓기
import math
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    tmp = math.comb(b, a)
    print(tmp)