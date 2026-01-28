"""
마라톤 16
맥주 99병 (B2)
문자열, 구현
"""

a = int(input())
for i in range(a, -1, -1):
    if i > 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        print()
    elif i == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer.")
        print("Take one down and pass it around, 1 bottle of beer on the wall.")
        print()
    elif i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
        print()
    else:
        if a > 1:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print(f"Go to the store and buy some more, {a} bottles of beer on the wall.")
        elif a == 1:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 1 bottle of beer on the wall.")
        
