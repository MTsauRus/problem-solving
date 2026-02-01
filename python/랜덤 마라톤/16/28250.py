"""
랜덤 마라톤 16
이브, 프시케, 그리고 푸른 MEX의 아내 (S2)
수학
"""
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
ans = 0

zero = 0
one = 0
more = 0

for now in l:
    if now == 0:
        zero+=1
        
    elif now == 1:
        one+=1
        
    else:
        more+=1

print((zero*one*2) + (zero*more) + (zero*(zero-1)//2))