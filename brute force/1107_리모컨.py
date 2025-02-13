## 리모컨 (G5)
import sys
input = sys.stdin.readline

N = int(input())
b = int(input())
if b == 0:
    print(min(len(str(N)), abs(100-N)))
    exit(0)
buttons = set(input().split()) # 사용 불가 buttons를 set 자료구조로 정의. 
if b == 10:
    print(abs(N-100))
    exit(0)
possibleNum = []
for i in range(1000000):
    now = set(str(i)) # 현재 숫자를 set으로. if i == 12345, set = [1, 2, 3, 4, 5]
    if not now.intersection(buttons): # 교집합이 0이면, 즉 사용 가능한 버튼으로만 이루어져있다면
        possibleNum.append(i)

before = 0
before_len = 0
if possibleNum[0] > N:
    print(min(abs(100-N), len(str(possibleNum[0]))+(possibleNum[0]-N)))
elif possibleNum[-1] < N:
    print(min(abs(100-N), len(str(possibleNum[-1]))+(N-possibleNum[-1])))
else:
    for next in possibleNum:
        length = len(str(next))
        if N == next:
            ans = length
            break
            
        else:    
            cnt = N - next
            if cnt > 0:
                before = cnt
                before_len = length
            else:
                ans = min(abs(cnt)+length, abs(before)+before_len)
                break
    print(min(abs(100-N), abs(ans)))