## 임스와 함께하는 미니게임 (S5)
## 자료구조
game = {'Y':1, 'F':2, 'O':3}
a, b = input().split()
S = set()
for _ in range(int(a)):
    S.add(input().strip())
print(len(S)//game[b])