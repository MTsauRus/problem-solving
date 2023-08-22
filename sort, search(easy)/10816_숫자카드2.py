### 숫자 카드 2 (S4)
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
cards = Counter(map(int, input().split()))
k = int(input())
needs = list(map(int, input().split()))
for i in needs:
    print(cards[i], end=" ")


