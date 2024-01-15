import sys
input = sys.stdin.readline
T = int(input())

def countDivisor(n, K):
    total = 0
    oddDiv = 0
    ans = 0
    
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                total += 1
                if i % 2 == 1:
                    oddDiv += 1
            else:
                total += 2
                if i % 2 == 1:
                    oddDiv += 1
                if (n // i) % 2 == 1:
                    oddDiv += 1
    evenDiv = total - oddDiv
    if evenDiv == K * oddDiv:
        ans += 1
    return ans

for i in range(T):
    N, K = map(int, input().split())
    print(countDivisor(N, K))
    
    
    
    