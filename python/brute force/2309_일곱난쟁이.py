### 일곱 난쟁이 (B1)
import sys
input = sys.stdin.readline

height = []
for _ in range(9):
    height.append(int(input()))
height.sort()

def foo():
    for i in range(9):
        for j in range(i, 9):
            tmp = sum(height) - height[i] - height[j]
            if tmp == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(height[k])
                return                    
foo()

