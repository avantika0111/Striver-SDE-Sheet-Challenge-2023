'''
Problem Statement: 
Given an array of N integers, 
write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.
'''

'''
OPTIMAL SOL USING MOORE"S VOTING ALGO
Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the count and find the expected majority element. 
    The second one is to check if the expected element is the majority one or not.
'''
def findMajorityElement(arr, n):

	# Step 1: applying Moore's Voting Algo
	cnt = 0

	for i in arr:
		if cnt == 0:
			ele = i
			cnt += 1
		else:
			if i == ele:
				cnt += 1
			else: 
				cnt -= 1
	
	# Step 2: check if ele is actually a majority element
	freq = 0
	if cnt > 0:
		for i in arr:
			if i == ele:
				freq += 1
	
	if freq > (n // 2):
		return ele
	
	return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = findMajorityElement(arr, len(arr))
print("The majority element is:", ans)