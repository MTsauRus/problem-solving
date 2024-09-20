"""
    마라톤  16
    대칭 차집합 (S4)
    자료구조
"""
import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
A = set((map(int, input().split())))
B = set((map(int, input().split())))

print(len(A.symmetric_difference(B)))