### selection sort ### 
import sys 
input = sys.stdin.readline
from collections import deque

# N = int(input())
# l = list(map(int, str(N)))
def selection_sort(l):
    for i in range(len(l)):
        max = l[i]
        max_idx = i
        for j in range(i, len(l)):
            if l[j] > max:
                max = l[j]
                max_idx = j
        l[i], l[max_idx] = l[max_idx], l[i]

### insertion sort ###
# times = []
# for i in range(1, N):
#     while i > 0 and times[i] < times[i-1]:
#         times[i], times[i-1] = times[i-1], times[i]
#         i = i-1
# 이거 맞나..?

### quick sort - 직관적인 방법 ###

def quick_sort_easy(arr):
    if len(arr) <= 1: 
        return arr

    pivot, tail = arr[0], arr[1:] # 첫 원소를 피벗으로
    leftside = [x for x in tail if x <= pivot]
    rightside = [x for x in tail if x > pivot]

    return quick_sort_easy(leftside) + [pivot] + quick_sort_easy(rightside)

### quick sort - classic ### 

def quick_sort(arr, start, end):
    if start >= end: # 원소가 1개이면
        return
    pivot = start # 첫번째 원소를 피벗으로
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1 # 왼쪽에서 피벗보다 큰 수를 찾을 때까지
        while right > start and arr[right] >= arr[pivot]:
            right -= 1 # 오른쪽에서 피벗보다 작은 수를 찾을 때까지
        if left > right: # 엇갈렸다면 피벗과 작은 수를 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 수와 큰 수를 서로 교체
            arr[left], arr[right] = arr[right], arr[left]
        
        quick_sort(arr, start, right - 1) 
        quick_sort(arr, right + 1, end) # 분할된 양쪽에서 다시 퀵소트 진행

    
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

def radix_sort(arr):
    buckets = [deque() for _ in range(10)]

    max_val = max(arr) # 배열의 최댓값 지정
    arr = deque(arr) # arr를 덱으로 변환
    num_of_digits = 1 # 자리수

    while max_val >= num_of_digits:
        while arr:
            num = arr.popleft()
            buckets[(num//num_of_digits) % 10].append(num) 

        for bucket in buckets:
            while bucket:
                arr.append(bucket.popleft()) # num_of_digits(1, 10, 100...)의 자리수 정렬
        
        num_of_digits *= 10

    return list(arr)

#print(radix_sort([5,2,6,19,22,19123,8534,3249]))


    