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

def _mergeSort(arr, low, high):
    if low >= high:
        return

    mid = floor((low + high) / 2)

    _mergeSort(arr, low, mid)
    _mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    # print(arr)

def mergeSort(arr, n):
    # Write your code here.
    _mergeSort(arr, 0, n-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
mergeSort(arr, n)
print(arr)