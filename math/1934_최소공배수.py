import sys
input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

n = int(input())
for _ in range(n):    
    a, b = map(int, input().split())
    print(a * b // GCD(a,b))