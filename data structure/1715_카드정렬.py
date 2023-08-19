### 카드 정렬하기(G4)
import sys
input = sys.stdin.readline
import heapq

N = int(input())
cards = []
sum = 0

for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    tmp = a + b
    sum += tmp
    heapq.heappush(cards, tmp)
print(sum)
    