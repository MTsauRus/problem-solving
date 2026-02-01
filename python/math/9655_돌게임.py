### 돌 게임 (S5)
import sys
input = sys.stdin.readline

a = int(input())
if a%2==0:
    print("CY")
else:
    print("SK")
"""
내 턴일 때 1, 3개가 있으면 승리, 2개가 있으면 패배

        A   B
    1   o   x
    2   x   o
    3   o   x
    4   x   o
    5   o   x
    6   x   o
    7   
    
"""