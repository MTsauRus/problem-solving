### 방 번호 (S5)
import sys
input = sys.stdin.readline
from collections import Counter
from math import ceil

N = list(map(int, input().strip()))
C = Counter(N)
C[6] += C[9]
C[9] = 0
C[6] /= 2
print(ceil(max(C.values())))