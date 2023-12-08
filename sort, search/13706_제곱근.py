### 제곱근 (S4)
import sys
input = sys.stdin.readline

a = int(input())
start = 1
rear = a
while True:
    mid = (start+rear)//2
    tmp = mid**2
    
    if tmp > a:
        rear = mid-1
    elif tmp < a:
        start = mid+1
    else:
        print(mid)
        break