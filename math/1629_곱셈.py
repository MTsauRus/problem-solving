### 곱셈 (S1)
### 수학, 분할정복을 이용한 거듭제곱, 모듈로 연산
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
def ans(a, b, c):
    result = 1
    base = a%c
    
    while b > 0:
        if b % 2 == 1:
            result *= base
        
        base *= base%c
        b //= 2
    
    return result%c

print(ans(a,b,c))