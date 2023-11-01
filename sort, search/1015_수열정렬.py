### 수열 정렬 (S4)
import sys
input = sys.stdin.readline

N = int(input())
tmp = list(map(int, input().split()))
num = []
for i in range(N):
    num.append([tmp[i], i])
num.sort()
for i in range(N):
    num[i].append(i)
num.sort(key=lambda x:x[1])
for i in range(N):
    print(num[i][2])