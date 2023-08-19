### 회의실 배정(S1)
import sys
input = sys.stdin.readline

N = int(input())
table = []
cnt = 0

for n in range(N):
    start, end = map(int, input().split())
    table.append((start, end))

table.sort(key = lambda x : (x[1], x[0]))

now = table.pop(0)
cnt += 1

for next in table:
    if now[1] <= next[0]: # 이전 종료 시각보다 다음 시작 시간이 작지 않다면
        cnt += 1
        now = next

print(cnt)
