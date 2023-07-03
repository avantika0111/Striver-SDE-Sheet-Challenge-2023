'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example:
|              _
|      _      | |_   _
|  _  | |_   _| | |_| |_
|_| |_| | |_| | | | | | |
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (block section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water are being trapped.

NOTE - HARD PROBLEM
'''

'''
Brute Force - If we observe carefully the amount the water stored at a particular index is 
the minimum of maximum elevation to the left and right of the index 
minus the elevation at that index.
Time Complexity: O(N*N) as for each index we are calculating leftMax and rightMax so it is a nested loop.

Space Complexity: O(1).
'''
def getTrappedWater1(arr, n):
    waterTrapped = 0
    for i in range(n):
        j = i
        leftMax = 0
        rightMax = 0
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        j = i
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        waterTrapped += min(leftMax, rightMax) - arr[i]
    return waterTrapped


'''
Better Approach - Using prefix sum and suffix sum.
Time Complexity: O(N) + O(2N) as we are traversing through the array only once and
computing prefix and suffix array.

Space Complexity: O(N)+O(N) for prefix and suffix arrays.
'''
def getTrappedWater2(arr, n) :
	ans = 0
	
	ps = 0
	prefixSum = [0] * n
	for i in range(n):
		ps = max(ps, arr[i])
		prefixSum[i] = ps

	ss = 0
	suffixSum = [0] * n
	for i in range(n-1, -1, -1):
		ss = max(ss, arr[i])
		suffixSum[i] = ss
	
	for i in range(n):
		ans += min(prefixSum[i], suffixSum[i]) - arr[i]
			
	return ans

'''
Optimal Approach using 2 pointers.
TC - O(N)
SC -O(1)
'''
def getTrappedWater3(arr, n):
    res = 0
    l = 0
    r = n - 1
    leftMax = 0
    rightMax = 0
    while l <= r:
        if arr[l] <= arr[r]:
            if arr[l] > leftMax:
                leftMax = arr[l]
            else:
                res += leftMax - arr[l]
            l += 1
        else:
            if arr[r] > rightMax:
                rightMax = arr[r]
            else:
                res += rightMax - arr[r]
            r -= 1
    return res

if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {getTrappedWater3(arr, len(arr))}")
