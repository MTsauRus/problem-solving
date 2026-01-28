### 어린 왕자 (S3)
import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

N = int(input())

for i in range(N):
    s1, s2, e1, e2 = map(int, input().split())
    n = int(input())
    ans = 0
    for j in range(n):
        x, y, r = map(int, input().split())
        s_dist = dist(x, y, s1, s2)
        e_dist = dist(x, y, e1, e2)
        r = float(r)
        if (s_dist < r and e_dist > r) or (s_dist > r and e_dist < r):
            ans += 1
    print(ans)