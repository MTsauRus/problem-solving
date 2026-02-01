## 쿠키의 신체 측정 (S4)
## 구현
import sys
input = sys.stdin.readline

a = int(input())
l = [[] for _ in range(a)]
ans = [0, 0, 0, 0, 0]
for i in range(a):
    l[i] = input().strip()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 심장의 좌표
def heart(a):
    for i in range(a):
        for j in range(a):
            if l[i][j] == '*':
                return [i+1, j]
            
heart = heart(a)
        
# 팔
left = l[heart[0]][:heart[1]]
right = l[heart[0]][heart[1]+1:]
for ch in left:
    if ch == '*':
        ans[0] += 1
for ch in right:
    if ch == '*':
        ans[1] += 1

# 허리
i = 1
while l[heart[0]+i][heart[1]] != '_':
    ans[2] += 1
    i+=1
leg_start = heart[0]+i

# 다리
for i in range(leg_start, a):
    if l[i][heart[1]-1] == '*':
        ans[3] += 1
for j in range(leg_start, a):
    if l[j][heart[1]+1] == '*':
        ans[4] += 1

heart[0]+=1
heart[1]+=1

print(*heart)
print(*ans)
    