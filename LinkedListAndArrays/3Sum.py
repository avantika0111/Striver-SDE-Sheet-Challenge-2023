
'''
We will try to optimize using 2 pointers approach.
TC - O(N^2) as we need two loops to find triplets.
SC - O(1)
'''
def findTriplets(arr, n, target):
    # using two pointers
    res = []
    arr.sort()
    for i in range(n - 2):
        if i == 0 or (i > 0 and arr[i] != arr[i - 1]):
            j = i + 1
            k = n -1
            reqSum = target - arr[i]
            while j < k:
                currSum = arr[j] + arr[k]
                if currSum < reqSum:
                    j += 1
                elif currSum > reqSum:
                    k -= 1
                else:
                    temp = [arr[i], arr[j], arr[k]]
                    res.append(temp)
                    while j < k and arr[j] == arr[j + 1]:
                        j += 1
                    while j < k and arr[k] == arr[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
    
    return res


if __name__ == '__main__':
    arr = [-1,0,1,2,-1,-4]
    k = 0
    print(f"The triplets with sum {k} are {findTriplets(arr, len(arr), k)}")