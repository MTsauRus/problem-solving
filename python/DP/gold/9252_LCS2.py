### 9252.LCS2 (G4)
### DP, LCS
import sys
input = sys.stdin.readline

a = ['0'] + list(input().strip())
b = ['0'] + list(input().strip())
D = [[0 for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            D[i][j] = D[i-1][j-1] + 1
        else:
            D[i][j] = max(D[i-1][j], D[i][j-1])
ans_len = D[-1][-1]
ans_str = ""
x, y = len(a)-1, len(b)-1
while D[x][y] > 0:
    nx1, ny1 = x-1, y
    nx2, ny2 = x, y-1
    if D[x][y] == D[nx1][ny1]:
        x, y = nx1, ny1
    elif D[x][y] == D[nx2][ny2]:
        x, y = nx2, ny2
    else:
        ans_str += a[x]
        x, y = x-1, y-1

print(ans_len)
ans = ""
for i in range(len(ans_str)-1, -1, -1):
    ans += ans_str[i]
print(ans) if len(ans) != 0 else exit(0)