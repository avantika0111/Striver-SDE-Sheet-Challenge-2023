'''
Problem Statement: Given an array of length 'N' that contains only 1 and 0 
Return the count of maximum consecutive 1's in the array when 'K' 0's are replaced by 1's.
'''
def longestSubSeg(arr, n, k):
    maxC = 0

    # zeroC will keep track of number of zeroes within max seq
    zeroC = 0

    # i will point to the first occurance of 1 in max seq
    # j will point to the last occurance of 1 in max seq
    i, j = 0, 0
    while j < n:
        
        if arr[j] == 0:
            zeroC += 1

        # reduce count of zero if it is more than k since we can only have k zeroes in max seq
        while zeroC > k:
            if arr[i] == 0:
                zeroC -= 1
            i += 1
        
        # max len will be maximum of j - i + 1 and max so far
        maxC = max(maxC, j - i + 1)
        j += 1

    return maxC

if __name__ == '__main__':
    arr = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1]
    k = 3
    print(f"Maximum consecutive ones are {longestSubSeg(arr, len(arr), k)}")