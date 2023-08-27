import sys
input = sys.stdin.readline

n = int(input())
# l = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
# for _ in range(n):
#     a, b = map(int, input().split())
#     a %= 10
#     b %= len(l[a])
    
#     ans = l[a][b-1]
#     if ans == 0:
#         ans = 10
        
#     print(ans)
for _ in range(n):
    a, b = map(int, input().split())
    ans = ((a%10)**(b%10))%10
    if ans == 0:
        print(10)
    else:
        print(ans)
    