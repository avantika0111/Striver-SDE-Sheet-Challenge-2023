'''
Problem Statement: Given an array containing both positive and negative integers, 
we have to find the length of the longest subarray with the sum of all elements equal to zero.
'''

'''
OPTIMAL APPROACH:
TC = O(N) = SC
'''

def LongestSubsetWithZeroSum(arr):
    n = len(arr)
    maxLen = 0
    s = 0
    hashset = {}
    for i in range(n):
        s = s + arr[i]
        if s == 0:
            maxLen = i + 1
        if arr[i] == 0 and maxLen == 0:
            maxLen = 1
        if s not in hashset:
            hashset[s] = i
        else:
            maxLen = max(maxLen, i - hashset[s])
    
    return maxLen

if __name__ == "__main__":
    arr = [1, 3, -1, 4, -4]
    print("Length of Longest Subarray with Zero sum is ",LongestSubsetWithZeroSum(arr))