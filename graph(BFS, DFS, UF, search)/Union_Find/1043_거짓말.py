### 거짓말 (G4)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
        
    if a in knownSet:
        parent[b] = a
    elif b in knownSet:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

people, party = map(int, input().split())
parent = [i for i in range(people + 1)]
known = list(map(int, input().split()))
knownNo = known.pop(0)
knownSet = set(known) # known을 set로 바꿈.

for i in range(knownNo - 1):
    union(known[i], known[i+1])


total_party = []
for i in range(party):
    group = list(map(int, input().split()))
    groupNo = group.pop(0)
    total_party.append(set(group))

    for j in range(groupNo - 1):
        union(group[j], group[j+1]) # party끼리 유니온.

for i in range(people+1):
    if find(i) in knownSet:
        knownSet.add(i)
ans = 0

for next_party in total_party:
    if not next_party.intersection(knownSet):
        ans += 1

print(ans)