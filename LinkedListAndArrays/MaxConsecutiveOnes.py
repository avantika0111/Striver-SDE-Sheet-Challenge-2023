'''
Problem Statement: Given an array that contains only 1 and 0 
Return the count of maximum consecutive ones in the array.
'''
def maxConsecutiveOnes(nums):
    cnt = 0
    maxCnt = 0
    for i in nums:
        if i == 1:
            cnt += 1
        else:
            cnt = 0
        maxCnt = max(maxCnt, cnt)
    return maxCnt

arr = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
print(f"Maximum consecutive ones are {maxConsecutiveOnes(arr)}")