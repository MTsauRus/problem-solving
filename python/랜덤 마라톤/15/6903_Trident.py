### 랜덤 마라톤 15
### Trident (B3)
### 구현

import sys
input = sys.stdin.readline

T = int(input())
S = int(input())
H = int(input())

l = "*" + " "*S + "*" + " "*S + "*"
space = " " * (len(l)//2)
for t in range(T):
    print(l)

for i in range(len(l)):
    print("*", end="")
    
print()

for h in range(H):
    print(space + "*")