import sys
l=["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]
a=int(input())
ll=[]
for i in range(a):
    ll.append(input().strip())

for next in ll:
    if next not in l:
        print("Yes")
        exit(0)
print("No")