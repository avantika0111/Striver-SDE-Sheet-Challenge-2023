from sys import maxsize
# Kadane's Algorithm
def maximumSubarraySum(arr, n):
    m = -maxsize - 1
    s = 0
    for i in range(n):
        s += arr[i]
        m = max(m, s)
        if s < 0:
            s = 0
    if m < 0:
        return 0
    return m

arr = list(map(int, input().split()))
n = len(arr)
print(maximumSubarraySum(arr, n))