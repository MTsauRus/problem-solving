### 잃어버린 괄호 (S2)
### 뇌절풀이
import sys
input = sys.stdin.readline

# remove_minus = input().strip().split('-')

# remove_plus = []
# ans_list = []

# for e in remove_minus:
#     remove_plus.append(e.split('+'))

# for element in remove_plus:
#     for k in range(len(element)):
#         i = 0
#         while element[k][i] == '0':
#             element[k] = element[k].replace('0', ' ', 1)
#             i += 1
#         element[k] = int(element[k].strip())
#     ans_list.append(sum(element))

# start = ans_list.pop(0)
# for next in ans_list:
#     start -= next

# print(start)

### 쉬운 방법
inputed = input().strip().split('-')
plus_splited = []
for element in inputed:
    tmpList = element.split('+')
    for ptr in range(len(tmpList)):
        tmpList[ptr] = int(tmpList[ptr])
    plus_splited.append(sum(tmpList))

ans = plus_splited.pop(0)
for next in plus_splited:
    ans -= next

print(ans)


