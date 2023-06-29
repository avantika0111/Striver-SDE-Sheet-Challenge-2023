def pairSum(arr, s):
    sett = set()
    ans = []
    for i in range(len(arr)):
        temp = s - arr[i]
        if (temp in sett):
            mini = min(temp, arr[i])
            maxi = max(temp, arr[i])
            ans.append([mini, maxi])
        sett.add(arr[i])

    ans.sort()

    return ans            

if __name__ == '__main__':
    arr = [2, 6, 5, 8, 11]
    target = 14
    res = pairSum(arr, target)
    print("The pairs with target sum are: ", res)
        
