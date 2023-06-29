"""
Problem statement: 
Given two sorted arrays arr1[] and arr2[] of sizes m and n 
in non-decreasing order. Merge them in sorted order. 
Modify arr1 so that it contains the first N elements and 
modify arr2 so that it contains the last M elements.
"""

"""
OPTIMAL SOL 1
Time Complexity: O(min(n, m)) + O(n*logn) + O(m*logm)
Reason: O(min(n, m)) is for swapping the array elements. 
    And O(n*logn) and O(m*logm) are for sorting the two arrays.
"""
def mergeSortedArrays1(arr1,arr2,m,n):
    left = m - 1
    right = 0

    while left >= 0 and right < n:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    arr1.sort()
    arr2.sort()

"""
MOST OPTIMAL SOLUTION AND PREFFERED IN INTERVIEWS:
Time Complexity: O((n+m)*log(n+m))
Reason: The gap is ranging from n+m to 1 and every time the gap gets divided by 2. 
    So, the time complexity of the outer loop will be O(log(n+m)). 
    Now, for each value of the gap, the inner loop can at most run for (n+m) times. 
    So, the time complexity of the inner loop will be O(n+m). 
    So, the overall time complexity will be O((n+m)*log(n+m)).
"""

def mergeSortedArrays2(arr1, arr2, m, n):
    
    gap = (m + n) // 2 + (m + n) % 2
    
    while gap > 0:
        left = 0
        right = left + gap

        while (right < m + n):
            # if left in arr[1] and right in arr[2]
            if left < m and right >= m:
                if arr1[left] > arr2[right - m]:
                    arr1[left], arr2[right - m] = arr2[right - m], arr1[left]
            
            # if left and right are in arr2
            elif left >= m:
                if arr2[left - m] > arr2[right - m]:
                    arr2[left - m], arr2[right - m] = arr2[right - m], arr2[left - m]
            
            # if both are in arr1
            else:
                if arr1[left] > arr1[right]:
                    arr1[left], arr1[right] = arr1[right], arr1[left]

            left += 1
            right += 1

        if gap == 1:
            break

        gap = (gap // 2) + (gap % 2)


if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    m = 4
    n = 3
    # mergeSortedArrays1(arr1, arr2, m, n)
    mergeSortedArrays2(arr1, arr2, m, n)
    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(m):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(n):
        print(arr2[i], end=" ")
    print()