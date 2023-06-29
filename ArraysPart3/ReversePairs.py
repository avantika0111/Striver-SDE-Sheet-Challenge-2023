from os import *
from sys import *
from collections import *
from math import *

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
        
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] =  temp[i -  low]

def countPairs(arr, low, mid, high):
    cnt = 0
    right = mid + 1
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2*arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def _mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt

    mid = floor((low + high) / 2)

    cnt += _mergeSort(arr, low, mid)
    cnt += _mergeSort(arr, mid+1, high)
    cnt += countPairs(arr, low, mid, high)
    merge(arr, low, mid, high)

    return cnt

def reversePairs(arr, n):
    # Write your code here.
    return _mergeSort(arr, 0, n-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
ans = reversePairs(arr, n)
print(ans)