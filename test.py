a=int(input())
l=list(map(int,input().split()))
test=[0]*10
for i in l:
    test[i]=1
for j in range(10):
    if test[j] == 1:
        print(j)