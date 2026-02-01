"""
    마라톤 16
    아기 석환 뚜루루 뚜루 (B1)
    문자열
"""
import sys
# mod 14
a = int(input())-1
b = a//14
a = a%14


if a == 0:
    print("baby")
elif a == 1:
    print("sukhwan")
elif a == 4:
    print("very")
elif a == 5:
    print("cute")
elif a == 8:
    print("in")
elif a == 9:
    print("bed")
elif a == 12:
    print("baby")
elif a == 13:
    print("sukhwan")
elif a == 2 or a == 6 or a == 10:
    if b >= 3:
        print("tu+"+"ru*"+str(b+2))
    elif b == 2:
        print("tururururu")
    elif b == 1:
        print("turururu")
    else:
        print("tururu")
else:
    if b >= 4:
        print("tu+"+"ru*"+str(b+1))
    elif b == 3:
        print("tururururu")
    elif b == 2:
        print("turururu")
    elif b == 1:
        print("tururu")
    else:
        print("turu")
    