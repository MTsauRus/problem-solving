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

def DFS(n):
    if len(str(n)) == N:
        print(n)

    else:
        for i in range(1, 10):
            if isPrime(n * 10 + i):
                DFS(n * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
