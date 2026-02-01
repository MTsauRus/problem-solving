### 27172. 수 나누기 게임 (G4)
### 수학, 소수 판정
import sys
input = sys.stdin.readline

def getDivisor(n):
    l = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            l.append(i) 
            if ( (i**2) != n) : 
                l.append(n // i)
    return l
    
n = int(input())
nums = list(map(int, input().split()))
used = set(nums)
score = [0 for _ in range(10**6 + 1)]
for num in nums:
    tmp_divisor = getDivisor(num)
    for next in tmp_divisor:
        if next in used:
            score[next] += 1
            score[num] -= 1
    
for num in nums:
    print(score[num], end=" ")
