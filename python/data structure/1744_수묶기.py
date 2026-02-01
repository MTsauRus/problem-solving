### 수 묶기
import sys
input = sys.stdin.readline
import heapq

N = int(input())
plusQ = []
minusQ = []
grouped_list = []
a, b = 0, 0
one = 0 # 1의 수
zero = 0 # 0의 수

for n in range(N):
    now = int(input())
    if now < 0:
        minusQ.append(now) # 0도 마이너스큐에. (0, -1) 이런식으로 묶어서 음수를 제거
    elif now > 1:
        plusQ.append(-now) # 최대 힙 사용을 위해 부호 뒤집음
    elif now == 1:
        one += 1
    else: # now == 0
        zero += 1

heapq.heapify(plusQ) 
heapq.heapify(minusQ) # 최대 힙으로

while len(plusQ) > 1:
    a = heapq.heappop(plusQ)
    b = heapq.heappop(plusQ)
    grouped_list.append(a*b)
if plusQ:
    grouped_list.append(-plusQ[0])

while len(minusQ) > 1:
    a = heapq.heappop(minusQ)
    b = heapq.heappop(minusQ)
    grouped_list.append(a*b)


if minusQ: # 원소 1개만 남아 있음.
    if zero == 0: # 음수를 지울 0이 없다면
        grouped_list.append(minusQ[0])
    # 0이 있다면, 0과 남은 음수를 곱해 없애줌.
    
while one > 0:
    grouped_list.append(1)
    one -= 1

print(sum(grouped_list))