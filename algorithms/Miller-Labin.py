prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

# def power_mod(a, b, mod):
#     res = 1
#     a %= mod
#     for i in range(b):

def power_mod(x, y, mod):
    ans = 1
    while y > 0:
        if y % 2:
            ans = (ans * x) % mod
        y //= 2
        x = x * x % mod
    return ans

print(power_mod(2, 9, 3 ))
def miller_rabin(a, p):
    k = p - 1
    while True:
        tmp = power_mod(a, k, p) # a^(p-1) % p
        if tmp == p - 1:
            return True
        k //= 2
        if k % 2 == 1: # k가 홀수라면, 즉 2^s * d에서 d만 남았다면
            break
    return (tmp == p - 1 or tmp == 1)





# def Miller_Rabin(a, p): # a는 밑, p는 판정할 수.
#     if a ** (p-1) % p == 1: # a^(p-1) % p == 1이면, p는 소수이다.(페르마 소정리)
#         return True
    
#     k = p - 1 # p가 소수인 홀수이면, k는 짝수이다.
#     while True:
#         tmp = power_mod(a, k, p)
#         if tmp == -1: return True # 인수 중 하나가 p에 의해 나누어 떨어짐. -> p는 소수
#         if k % 2 == 1: # k가 홀수->a^2^(s-1)*d에서, d만 남음. 즉, k^d인 상태이며, 이는 최종항까지 도달했음을 의미
#             return tmp == 1 or tmp == p - 1
#             # 최종항에서의 마지막 검사. (a^d + 1)(a^d - 1) 중, p에 의해 나누어 떨어진다면 이는 소수를 의미.
#         k /= 2 # k를 계속해서 줄여나감. 이는 s-1, s-2, s-3과 같은 효과.

print(miller_rabin(2, 41))
    
    
    
    
    
    
    
    
    
    
    
    
    
    # tmp = p - 1
    # s = 0
    # while tmp % 2 == 0: # s를 구하자.
    #     s += 1
    #     tmp //= 2

    # x = (a ** (p - 1)) % p
    # for _ in range(s):
    #     if x == p-1 or x == 1:
    #         return True
        
    #     else:
    #         x = (x ** 2) % p
    #         if x == p-1:
    #             return True
    
    # return False

# print(Miller_Rabin(2, 3))
    # k = p - 1 # k는 a의 지수.
    # while True:
    #     tmp = (a**k) % p 
    #     if tmp == p - 1: # a^k == -1 (mod p)
    #         return True
    #     if tmp 


