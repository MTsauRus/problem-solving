### 1644. 소수의 연속합 (G3)
### 소수 판정, 투 포인터
import sys
input = sys.stdin.readline

def find_prime(n):
    is_prime = [False, False] + ([True]*(n-1))
    for i in range(2, int(n**0.5)+1):
        for j in range(i*2, n+1, i):
            if is_prime:
                is_prime[j] = False
                
    prime = []
    for i in range(n+1):
        if is_prime[i]:
            prime.append(i)
    return prime

n = int(input())
if n == 1:
    print(0)
    exit(0)

ans = 0
prime = find_prime(n)
limit = len(prime)

s, e = 0, 0
current_sum = prime[s]
while s <= e:
    if current_sum == n:
        ans += 1
        current_sum -= prime[s]
        s += 1
    
    elif current_sum < n:
        if e == limit-1: 
            break
        e += 1
        current_sum += prime[e]
    else:
        current_sum -= prime[s]
        s += 1
        
print(ans)