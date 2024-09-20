<<<<<<< HEAD
### 수들의 합 (S5)
### 수학, 그리디
import sys
input = sys.stdin.readline

a = int(input())
b = 1
sum = 0
while True:
    sum += b
    if sum > a:
        print(b-1)
        break
    elif sum == a:
        print(b)
        break
    else:
        b += 1
=======
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
    
>>>>>>> 703ed7412d4a72897df5ccc1a2fe4cb902eb0b8c
