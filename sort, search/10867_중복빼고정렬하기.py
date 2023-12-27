### 중복 빼고 정렬하기 (S5)
import sys
input = sys.stdin.readline

N = int(input())
s = set(map(int, input().split()))
l = list(s)
l.sort()
print(*l)
