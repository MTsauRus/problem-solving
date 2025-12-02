T=int(input())
for t in range(1,T+1):
    N,K=map(int,input().split())
    nums=list(map(int,input().split()))
    D=[0 for _ in range(K+1)] # 합이 K가 되는 수열의 수
    D[0]=1
    for num in nums:
        for i in range(K,num-1,-1): 
            D[i]+=D[i-num]
    print(f'#{t} {D[K]}')