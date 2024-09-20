### 수들의 합 (S5)
### 수학, 그리디
import sys
input = sys.stdin.readline

a = int(input())
b = 1
sum = 0
while True:
    sum += b
    if sum > a:
        print(b-1)
        break
    elif sum == a:
        print(b)
        break
    else:
        b += 1