### 숫자 카드 (S5)
import sys
input = sys.stdin.readline

### binary search 풀이

# n = int(input())
# cards = list(map(int, input().split()))
# k = int(input())
# needs = list(map(int, input().split()))

# ans = []

### binary search 풀이
# ans = []
# cards.sort()

# for next in needs:
#     front = 0
#     rear = n-1
#     mid = (front+rear) // 2
#     find = False

#     while front <= rear:
#         mid = (front+rear) // 2
#         if next > cards[mid]:
#             front = mid + 1

#         elif next < cards[mid]:
#             rear = mid - 1

#         else:
#             find = True
#             break
    
#     if find: ans.append(1)
#     else: ans.append(0)

# print(*ans)
        
### 날먹풀이
n = int(input())
cards = set(map(int, input().split()))
k = int(input())
wants = list(map(int, input().split()))
ans = []
for next in wants:
    if next in cards: ### set에서 in은 시간복잡도가 1
        ans.append(1)
    else:
        ans.append(0)

print(*ans)