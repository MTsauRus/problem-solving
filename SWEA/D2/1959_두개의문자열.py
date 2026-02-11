### 1959. 두 개의 문자열 (D2)
T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    
    tmpa = list(map(int, input().split()))
    tmpb = list(map(int, input().split()))
    if a > b:
        long = tmpa
        short = tmpb
    else:
        long = tmpb
        short = tmpa
    ans = -float('inf')
    
    for i in range(len(long)-len(short)+1):
        tmp_sum = 0
        for j in range(len(short)):
            tmp_sum += long[i+j]*short[j]
        
        ans = max(ans, tmp_sum)

    print(f'#{t} {ans}')