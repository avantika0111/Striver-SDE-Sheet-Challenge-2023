def nextPermuation(arr):
    n = len(arr)

    # step 1: find the breakpoint to get the longest prefix
    idx = -1
    for i in range(n-2, -1, -1):
        if arr[i]<arr[i+1]:
            idx = i
            break

    # Edge Case: when the given array is having highest permutation
    if(idx == -1):
        return arr[::-1]

    # step 2: find the next greatest number and swap it with the breakpoint element
    for i in range(n-1, idx, -1):
        if arr[i] > arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            break
    
    # step 3: rev the elements after the prefix
    arr[idx+1:] = arr[idx+1:][::-1]
    return arr

arr = list(map(int, input().split()))
print(nextPermuation(arr))