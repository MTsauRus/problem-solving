import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
ans = []

def isPrime(num):
    if num == 0:
        return False
    elif num == 1:
        return False
    else:
        for i in range(2, int(num**0.5+1)):
            if num % i == 0:
                return False
        return True

def amazing_prime(i, N):
    if N == 0 : return
    for _ in range(10):
        if isPrime(i):
            if N == 1:
                ans.append(i)

            amazing_prime(i*10, N-1)
        i += 1

amazing_prime(0, N)

for a in ans:
    print(a)