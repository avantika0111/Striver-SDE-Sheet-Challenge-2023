def rotateMatrixElementsClockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    while left < right and top < bottom:
        prev = matrix[top+1][left]
        for i in range(left, right+1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr
        top += 1

        for i in range(top, bottom+1):
            curr = matrix[i][right]
            matrix[i][right] = prev
            prev = curr
        right -= 1

        for i in range(right, left-1, -1):
            curr = matrix[bottom][i]
            matrix[bottom][i] = prev
            prev = curr
        bottom -= 1

        for i in range(bottom, top-1, -1):
            curr = matrix[i][left]
            matrix[i][left] = prev
            prev = curr
        left += 1

    return matrix


r = int(input())
c = int(input())
matrix = []
for i in range(r):
    row = list(map(int, input().split()))[:c]
    matrix.append(row)
print(rotateMatrixElementsClockwise(matrix))
