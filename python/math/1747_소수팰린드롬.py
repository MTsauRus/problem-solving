### 소수&팰린드롬 (S1)
import sys
input = sys.stdin.readline
limit = 1200000

def seive(N):
    prime = [False, False] + [True] * (limit - 1)
    for i in range(2, int(limit ** 0.5 + 1)):
        if prime[i] == True:
            for j in range(i * 2, limit + 1, i):
                prime[j] = False
        
    return [x for x in range(N, limit + 1) if prime[x] == True]

def palindrome(N):
    now = list(str(N))
    flag = True
    for i in range(len(now) // 2):
        if now[i] != now[-(i + 1)]:
            flag = False
    
    return flag

N = int(input())
prime = seive(N)

for p in prime:
    if palindrome(p):
        print(p)
        break