def removeDuplicates(arr,n):
    i = 0
    for j in range(n):
        if arr[i] != arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i + 1

if __name__ == '__main__':
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    n = len(arr)
 
    # removeDuplicates() returns new size of array.
    n = removeDuplicates(arr, n)
 
    # Print updated array
    for i in range(n):
        print("%d" % (arr[i]), end=" ")