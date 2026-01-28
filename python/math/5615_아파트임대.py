### 아파트 임대 (P1)
import sys
input = sys.stdin.readline

rabin_num = [2, 7, 61] # for 2^31 - 1
def power_mod(a, b, mod):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans = ans * a % mod
        a = a * a % mod
        b //= 2

    return ans 

def miller_rabin(a, p):
    k = p - 1

    while True:
        tmp = power_mod(a, k, p)
        if tmp == p - 1:
            return True
        k //= 2
        if k % 2 == 1: # k가 홀수: 2^s*d에서 d만 남음.(d는 홀수)
            break
        
    tmp = power_mod(a, k, p)
    return (tmp == 1 or tmp == p - 1) # (a^d+1)(a^d-1)

def seive(lim): # 에라토스테네스
    prime = [False, False] + [True] * (lim - 1)
    for i in range(2, int(lim ** 0.5) + 1):
        if prime[i]:
            for j in range(i * 2, lim + 1, i):
                prime[j] = False
    return [x for x in range(lim+1) if prime[x] == True]

def is_prime(p):
    prime_under_100 = seive(100)
    if p <= 1:
        return False
    
    elif 1 < p and p <= 100:
        return p in prime_under_100
    else:
        for test in rabin_num:
            if not miller_rabin(test, p):
                return False
        return True
    
N = int(input())
cnt = 0
apart = []
for _ in range(N):
    next = int(input()) * 2 + 1
    if is_prime(next):
        cnt += 1

print(cnt)


