### 2467 용액
### 구현, 투 포인터
import sys
input = sys.stdin.readline

## 양수/음수로 나누고 양 극단을 더하자. 
## 양수인 경우 양수 크기를 줄여야 함 (양수 포인터 -=1)
## 음수인 경우 음수 크기를 줄여야 함 (음수 포인터 +=1)
## 0인 경우 탐색 종료, 두 포인터가 만나는 경우 탐색 종료
def sol():
    N = int(input())
    l = list(map(int, input().split()))
    pivot = float('inf')
    if l[0] >= 0: # 모두 양수로 주어지는 경우
        print(l[0], l[1])
        return
    elif l[-1] < 0: # 모두 음수로 주어지는 경우
        print(l[-2], l[-1])
        return
    else:
        plus, minus = N-1, 0
        while (plus > minus):
            tmp = l[plus] + l[minus]
            if pivot > abs(tmp):
                pivot = abs(tmp)
                ans = [l[minus], l[plus]]
            if tmp == 0:
                break
            elif tmp > 0: # 두 합이 양수: 양수 크기 줄이기
                plus -= 1
            else: # 두 합이 음수: 음수 크기 줄이기
                minus += 1

    print(ans[0], ans[1])
    return

sol()