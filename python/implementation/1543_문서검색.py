### 1543. 문서 검색(S5)
### 문자열, 구현
import sys
input = sys.stdin.readline

L = input().strip()
want = input().strip()
ans = 0
i = 0
while i < len(L)-len(want)+1:
    if L[i:i+len(want)] == want:
        ans += 1
        i += len(want)
        continue
    i += 1

print(ans)