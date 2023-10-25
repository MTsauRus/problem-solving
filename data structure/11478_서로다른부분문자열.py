### 서로 다른 부분 문자열의 개수 (S3)
import sys
input = sys.stdin.readline

a=input().strip()
length=len(a)
s = set()
for i in range(length):
    for j in range(0, length, 1):
        s.add(a[j:j+i])

print(len(s))