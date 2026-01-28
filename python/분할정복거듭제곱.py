def power(x, n):
    result = 1
    base = x
    
    while n > 0:
        if n % 2 == 1: # 홀수이면
            result *= base
        
        base *= base
        n //= 2
        
    return result

a, b = map(int, input().split())
print(power(a,b))