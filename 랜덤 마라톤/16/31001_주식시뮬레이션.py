"""
마라톤 16
주식 시뮬레이션 (S1)
구현
"""
import sys
input = sys.stdin.readline

global stocks, my, balance
stocks = [] # [이름, 그룹번호, 주가]
my = [] # [보유주식이름, 보유주식그룹, 주수]
balance = 0

def func(Q):
    global stocks, my, balance
    if 1 <= int(Q[0]) <= 3:
        stock_name, n = Q[1], int(Q[2])
        for tmp in stocks:
            if tmp[0] == stock_name:
                stock_now = tmp # stock_now: 다룰 주식
                break
            
        for tmp in my:
            if tmp[0] == stock_name:
                stock_my = tmp
                break
            stock_my = 0 # 해당 주식을 보유하지 않음
        
        if Q[0] == '1': # Q[1, 주식이름, 주수]
            total_price = stock_now[2] * n
            if balance >= total_price:
                my.append([stock_name, stock_now[1], n])
                balance -= total_price
        
        elif Q[0] == '2':
            if stock_my == 0:
                return
            if n >= stock_my[2]:
                my.
    
    # if Q[0] == '1': # (1, 주식이름, 주수)
    #     stock_name, n = Q[1], int(Q[2])
    #     for tmp in stocks:
    #         if stock_name == tmp[0]:
    #             now = tmp # now: 현재 다룰 주식
        
    #     total_price = stocks[stock_name][1] * n
    #     if balance >= total_price:
    #         my.append([stocks[stock_name][0], stock_name, n])
    #         balance -= total_price
            
    # elif Q[0] == '2': # (2, 주식이름, 주수)
    #     stock_name, n = Q[1], int(Q[2])
        
        
    
N, balance, q = map(int, input().split())
for _ in range(N): # 주식 입력
    group, name, price = input().split()
    stocks[name] = [int(group), int(price)]
    
for _ in range(q):
    query = list(input().split())
    func(query)
    print(my)
    print(stocks)
    print(balance)
            