### 문자열 집합(S3)
import sys
input = sys.stdin.readline

A, B = map(int, (input().split()))
S = set()
for i in range(A):
    S.add(input().strip())
ans = 0
for j in range(B):
    if input().strip() in S:
       ans += 1
print(ans) 