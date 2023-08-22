# import sys
# from collections import deque
# import heapq
# input = sys.stdin.readline

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr # 재귀 종료 조건. 
    
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid]) # 앞부분
#     high_arr = merge_sort(arr[mid:]) # 뒷부분
    
#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr): # 포인터
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             h += 1
#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    l = r = 0
    merged = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    merged += left[l:]
    merged += right[r:]
    return merged

l = [1,5,3,2,4]
print(merge_sort(l))