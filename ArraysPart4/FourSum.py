'''
4 Sum | Find Quads that add up to a target value
'''

'''
OPTIMAL APPROACH:
Time Complexity: O(N3), where N = size of the array.
Reason: Each of the pointers i and j, is running for approximately N times. 
And both the pointers k and l combined can run for approximately N times including the operation of skipping duplicates. 
So the total time complexity will be O(N3). 
'''
def fourSum(nums, target):
    n = len(nums)
    nums.sort()
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n):
            if j != i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s < target:
                    k += 1
                elif s > target:
                    l -= 1
                else:
                    quad = [nums[i], nums[j], nums[k], nums[l]]
                    res.append(quad)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
    
    return res
'''
Another Sol that is based on hashing. but fails on below TC
TC = O(N^2) = SC
'''
def findCommon(p1, p2):
    return p1[0] == p2[0] or p1[0] == p2[1] or p1[1] == p2[0] or p1[1] == p2[1]

def fourSum2(nums, target):
    n = len(nums)
    res = []
    
    mp = {}
    for i in range(n-1):
        for j in range(i+1, n):
            mp[nums[i] + nums[j]] = [i, j]
    # print(mp)
    for i in range(n-1):
        for j in range(i+1, n):
            s = nums[i] + nums[j]
            if target - s in mp and not findCommon(mp[target - s], [i, j]):
                temp = []
                temp.append(nums[mp[target - s][0]])
                temp.append(nums[mp[target - s][1]])
                temp.append(nums[i])
                temp.append(nums[j])
                temp.sort()
                if temp not in res:
                    res.append(temp)
    res.sort()
    return res

if __name__ == '__main__':
    nums = [-4,-3,-2,-1,0,0,1,2,3,4]
    target = 0
    ans = fourSum(nums, target)
    ans2 = fourSum2(nums, target)
    print("The quadruplets from 1st function are:")
    for it in ans:
        print("[", end="")
        for ele in it:
            print(ele, end=" ")
        print("]", end=" ")
    print()
    print("The quadruplets from 2nd function are:")
    for it in ans2:
        print("[", end="")
        for ele in it:
            print(ele, end=" ")
        print("]", end=" ")
    print()