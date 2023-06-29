'''
Problem Statement: Given a matrix m X n, 
count paths from left-top to the right bottom of a matrix 
with the constraints that from each cell 
you can either only move to the rightward direction or the downward direction.
'''

'''
DP SOLUTION:
Time Complexity: The time complexity of this solution will be O(n*m) 
because at max there can be n*m number of states.

Space Complexity: As we are using extra space for the dummy matrix 
the space complexity will also be O(n*m).
'''
def uniquePathUtil(i, j, m, n, dp):
	if i == m - 1 and j == n - 1:
		return 1
	if i >= m or j >= n:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	else:
		dp[i][j] = uniquePathUtil(i+1, j, m, n, dp) + uniquePathUtil(i, j+1, m, n, dp)
		return dp[i][j]


def uniquePathsDP(m, n):
	# DP Solution
	dp = [[-1 for x in range (n)] for y in range(m)]  
	return uniquePathUtil(0, 0, m, n, dp)



'''
MOST OPTIMAL SOL:
Time Complexity: The time complexity of this solution will be O(n-1) or  O(m-1) 
depending on the formula we are using.

Space Complexity: O(1).
'''
def uniquePathsNCR(m, n):
	# nCr solution
	N = n + m -2
	r = m - 1
	res = 1
	for i in range(1, r + 1):
		res = res * (N - r + i) / i
	return int(res)

if __name__ == "__main__":
    totalCount = uniquePathsNCR(3, 7)
    # totalCount = uniquePathsDP(3, 7)
    print("The total number of Unique Paths are ", totalCount)