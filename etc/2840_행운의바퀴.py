### 행운의 바퀴 (S4)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = ['?'] * N
ptr = 0

for i in range(K):
    tmp = list(input().split())
    ptr += int(tmp[0])
    ptr %= N
    if ans[ptr] == "?":
        if tmp[1] in ans:
            print("!")
            exit(0)
        else:
            ans[ptr] = tmp[1]
    elif ans[ptr] == tmp[1]:
        continue
    else:
        print("!")
        exit(0)

ans.reverse()
ptr = (N-1) - ptr
for i in range(ptr, N):
    print(ans[i], end="")
for j in range(0, ptr):
    print(ans[j], end="")