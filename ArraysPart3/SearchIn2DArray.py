'''
Binary Search Method
TC - O(log(m*n))
'''
def searchMatrix(mat, target):
    # Write your code here.
    if len(mat) == 0:
        return False

    n = len(mat)
    m = len(mat[0])

    low = 0
    high = (n * m) - 1

    while low <= high:
        mid = (low + (high - low) // 2)
        if mat[mid // m][mid % m] == target:
            return True
        elif mat[mid // m][mid % m] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == '__main__':
    mat = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
    target = 8
    if searchMatrix(mat, target):
        print("Target is present in matrix")
    else:
        print("Target is not in matrix")