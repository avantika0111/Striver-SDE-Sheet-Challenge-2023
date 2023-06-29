"""
Problem Statement: 
Given an array of N + 1 size, where each element is between 1 and N. 
Assuming there is only one duplicate number, 
your task is to find the duplicate number.
"""

"""
OPTIMAL SOL:
TC: O(N), SC: O(1)
"""
def findDuplicate(arr):
    slow = arr[0]
    fast = arr[arr[0]]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    fast = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

if __name__ == "__main__":
    arr = [3, 1, 3, 4, 2]
    print("The duplicate element is ", findDuplicate(arr))
