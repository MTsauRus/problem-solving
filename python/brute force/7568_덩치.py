import sys
input = sys.stdin.readline

N = int(input())
big = []
for i in range(N):
    big.append(tuple(map(int, input().split())))
ans = []
for i in range(N):
    cnt = 1
    now = big[i]
    for j in range(N):
        tmp = big[j]
        if now[0] < tmp[0] and now[1] < tmp[1]:
            cnt += 1
            
    ans.append(cnt)
    
print(*ans)