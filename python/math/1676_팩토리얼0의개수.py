### 팩토리얼 0의 개수 (S5)
import sys
input = sys.stdin.readline

N = int(input())
two = 0
five = 0
for n in range(2, N+1):
    while n % 2 == 0:
        n //= 2
        two += 1
    
    while n % 5 == 0:
        n //= 5
        five += 1
if two != 0 and five != 0:
    if two >= five:
        print(five)
    else:
        print(two)
else:
    print(0)

