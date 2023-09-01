### 수 찾기(S4) 
import sys
input = sys.stdin.readline

length = int(input())
num = list(map(int, input().split()))
iteration = int(input())
need = list(map(int, input().split()))

def search(num, key): # num: sorted list
    front = 0
    rear = len(num) - 1
    while front <= rear:
        mid = (front + rear) // 2

        if num[mid] > key:
            rear = mid - 1

        elif num[mid] < key:
            front = mid + 1

        else:
            return 1
        
    return 0

num.sort()
for i in need:
    print(search(num, i))

