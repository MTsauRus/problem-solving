## 이항 계수 구하기 문제 ##
# 1. 파스칼의 삼각형 직접 구현
def paskal(n, r):
    # (n+1)*(r+1) 배열을 만듦.
    paskal_triangle = [[0 for _ in range(r+1)] for _ in range(n+1)]
    for i in range(n+1):
        paskal_triangle[i][0] = 1 # 파스칼의 iC0 = 1
    for i in range(r+1):
        paskal_triangle[i][i] = 1 # 파스칼의 iCi = 1

    for i in range(1, n+1):
        for j in range(1, r+1):
            paskal_triangle[i][j] = paskal_triangle[i-1][j] + paskal_triangle[i-1][j-1]
        
    return paskal_triangle
print(paskal(10, 5))

## 2. 동적 계획법 - 완전탐색 memorization
## n번의 기회 중 k번 뽑는 경우의 수.
# func(times, got) : 그동안 times만큼의 기회, 그 중 got만큼 선택
# n번째에 다다랐을 때 k개를 선택하는 경우의 수.
# times = n and got = k일 때 return 1. if not: return 0
def bino_coef(n, k):
    if k > n:
        return 0 # kCn에서 k가 더 크면 당연히 경우의 수는 0
    # 캐시 초기화
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def choose(times, got):
        if times == n:
            return got == k # times == n, got == k이면 1을 반환. 아니면 0 반환
        # -1이 아니면, 즉 계산한 적이 있다면
        if cache[times][got] != -1:
            return cache[times][got] # 다시 계산하지 말고 바로 반환

        # 위의 조건문에서 걸러지지 않음 == -1 == 계산해야 함. 
        #     
        cache[times][got] = choose(times+1, got) + choose(times+1, got+1)
        return cache[times][got]
    
    return choose(0, 0)
        
