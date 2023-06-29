'''
Problem Statement: Given an array of N integers. 
Find the elements that appear more than N/3 times in the array. 
If no such element exists, return an empty vector.
'''
from sys import *
"""
Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the counts and find the expected majority elements. 
    The second one is to check if the calculated elements are the majority ones or not.
"""
def majorityElementII(arr):
	# Write your code here.
	n = len(arr)
	res = []

	# Step 1: applying modified Moore's Voting Algo
	cnt1, cnt2 = 0, 0
	ele1, ele2 = -maxsize, -maxsize

	for i in arr:
		if cnt1 == 0 and i != ele2:
			ele1 = i
			cnt1 += 1
		elif cnt2 == 0 and i != ele1:
			ele2 = i
			cnt2 += 1
		elif i == ele1:
			cnt1 += 1
		elif i == ele2:
			cnt2 += 1
		else: 
			cnt1 -= 1
			cnt2 -= 1
 	
	# Step 2: check if ele is actually a majority element
	freq1 = 0
	freq2 = 0
	for i in arr:
		if i == ele1:
			freq1 += 1
		if i == ele2:
			freq2 += 1
	
	if freq1 > (n // 3):
		res.append(ele1)
	if freq2 > (n // 3):
		res.append(ele2)
		
	
	return res

arr = [11, 33, 33, 11, 33, 11]
ans = majorityElementII(arr)
print("The majority elements are: ", end="")
for it in ans:
    print(it, end=" ")
print()