### 듣보잡 (S4)
a, b = map(int, input().split())
A, B = set(), set()
for _ in range(a):
    A.add(input().strip())
for _ in range(b):
    B.add(input().strip())
ansSet = sorted(list(A.intersection(B)))
print(len(ansSet))
for next in ansSet:
    print(next)

