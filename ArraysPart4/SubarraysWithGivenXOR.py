'''
Problem Statement: Given an array of integers A and an integer B. 
Find the total number of subarrays having bitwise XOR of all elements equal to k.
'''

'''
OPTIMAL APPROACH USING HASHING
Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, 
where N = size of the array.
Reason: For example, if we are using an unordered_map data structure in C++ 
the time complexity will be O(N) but if we are using a map data structure, 
the time complexity will be O(N*logN). 
The least complexity will be O(N) as we are using a loop to traverse the array. 
Point to remember for unordered_map in the worst case, 
the searching time increases to O(N), 
and hence the overall time complexity increases to O(N2). 

Space Complexity: O(N) as we are using a map data structure.
'''

def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    n = len(arr)
    cnt = 0
    xr = 0
    mp = {}
    mp[xr] = 1
    for i in range(n):
        xr = xr ^ arr[i]
        firstXOR = xr ^ x
        if firstXOR in mp:
            cnt += mp[firstXOR]
        if xr not in mp:
            mp[xr] = 1
        else:
            mp[xr] += 1
    
    return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysXor(a, k)
    print("The number of subarrays with XOR k is:", ans)