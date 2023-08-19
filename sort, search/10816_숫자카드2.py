### 숫자 카드 2 (S4)
### set 구조 사용, 중복된 수에 따로 cnt++ 관리

n = int(input())
tmp = list(map(int, input().split()))
k = int(input())
needs = list(map(int, input().split()))
cards = set()

tmp.sort()

for next in tmp:
    if next in cards:
        
