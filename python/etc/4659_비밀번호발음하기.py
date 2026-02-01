### 비밀번호 발음하기 (S5)
### 구현, 문자열
import sys
input = sys.stdin.readline

def aeiou(a):
    for token in a:
        if token in 'aeiou':
            return True
    return False

def not_aeiou(a):
    for token in a:
        if token not in 'aeiou':
            return True
    return False

def rule2(a):
    for i in range(len(a)-2):
        all_vowels = aeiou(a[i]) and aeiou(a[i+1]) and aeiou(a[i+2])
        not_all_vowels = not_aeiou(a[i]) and not_aeiou(a[i+1]) and not_aeiou(a[i+2])
        if all_vowels or not_all_vowels:
            return False
    return True

def rule3(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            if a[i] not in 'eo':
                return False
    return True

while True:
    a = input().strip()
    if a == 'end':
        break
    
    if not aeiou(a):
        print('<'+a+'> is not acceptable.')
        continue
    
    if len(a) == 1:
        print('<'+a+'> is acceptable.')
        continue
    
    elif len(a) == 2:
        if a[0] in 'aiu' and a[0] == a[1]:
            print('<'+a+'> is not acceptable.')
        else:
            print('<'+a+'> is acceptable.')
        continue
    
    else:
        if rule2(a) and rule3(a):
            print('<'+a+'> is acceptable.')
        else:
            print('<'+a+'> is not acceptable.')