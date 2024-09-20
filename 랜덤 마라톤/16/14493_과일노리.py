"""
    랜덤 마라톤 16
    과일노리 (S5)
    구현, 수학
"""
import sys
n = int(input())
bot = []

_, ans = map(int, input().split())
ans += 1

for __ in range(n-1):
    bot.append(list(map(int, input().split())))

for now in bot:
    delay, check = now[0], now[1]
    if ans < delay:
        ans += 1
        continue
    else:
        tmp = (ans - check)%(delay + check)
    
    if tmp < delay: # 바로 갈 수 있는 경우
        ans += 1
        
    else: # 봇이 동작중인 경우: 봇의 남은 시간만큼 기다려야 함
        ans += (delay + check - tmp)+1
        
print(ans)