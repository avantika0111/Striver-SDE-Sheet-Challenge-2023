'''
Problem Statement: You are given an array of N integers. 
You need to find the length of the longest sequence which contains the consecutive elements.
'''


'''
OPTIMAL SOL:
TC = O(N) = SC
'''
def lengthOfLongestConsecutiveSequence(arr):
    maxCnt = 1
    hashset = set()
    for i in arr:
        hashset.add(i)
    
    for i in arr:
        if i - 1 not in hashset:
            j = i
            while j in hashset:
                j += 1
            maxCnt = max(maxCnt, j - i)

    return maxCnt


if __name__ == "__main__":
    arr = [100, 200, 1, 2, 3, 4]
    lon = lengthOfLongestConsecutiveSequence(arr)
    print("The longest consecutive sequence is", lon)