import random
l = ['아', '오', '키', '지', '센', '고', '쿠', '키', '자', '루', '몽', '키', '디', 
     '루', '피', '거', '프', '아', '카', '이', '누']

line, n = map(int, input().split())


for i in range(line):
    s = ""
    past = 0
    for j in range(n):
        rand = random.randint(0, 20)
        while past == rand:
            rand = random.randint(0, 20)
        s+=l[rand]
        past = rand
    print(s)