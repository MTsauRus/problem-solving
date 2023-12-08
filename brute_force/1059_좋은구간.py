### 좋은 구간 (S4)
import sys
input = sys.stdin.readline

a = int(input())
l = list(map(int, input().split()))
N = int(input())
l.append(N)
l.sort()
front = l[l.index(N)-1]
rear = l[l.index(N)+1]
if front == N or rear == N:
    print(0)

else:
    if front > N:
        front = 0
    ans = 0
    for i in range(front+1, N):
        ans += rear-N
    ans += (rear-N-1)
    print(ans)
