### 1080. 행렬 (S1)
### 그리디
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
a, b = [], []

for _ in range(R):
    a.append(list(map(int, input().strip())))
for _ in range(R):
    b.append(list(map(int, input().strip())))

if a == b:
    print(0)
    exit(0)
if R < 3 or C < 3:
    print(-1)
    exit(0)
    
ans = 0
for r in range(R-2):
    for c in range(C-2):
        if a[r][c] != b[r][c]:
            ans += 1
            for i in range(3):
                for j in range(3):
                    if a[r+i][c+j]:
                        a[r+i][c+j] = 0
                    else:
                        a[r+i][c+j] = 1
for r in range(R):
    for c in range(C):
        if a[r][c] != b[r][c]:
            print(-1)
            exit(0)

print(ans)