a,b=map(int,input().split())
ans = 0
for i in range(a):
    l=list(input().strip())
    tmpcnt=0
    for j in l:
        if j == 'O':
            tmpcnt+=1
    if float(tmpcnt)>=b/2:
        ans+=1
print(ans)        
    