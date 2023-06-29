"""
Problem Statement: 
You are given a read-only array of N integers with values also in the range [1, N] 
both inclusive. Each integer appears exactly once except A which appears twice 
and B which is missing. The task is to find the repeating and missing numbers A and B 
where A repeats twice and B is missing.
"""

"""
OPTIMAL SOL 1:
TC = O(N) 

S - Sn = X - Y .....equation 1
S2-S2n = X2-Y2 .....equation 2
X+Y = (S2 - S2n) / (X-Y)
X+Y = (S2 - S2n) / (S - Sn) ....equation 3
From eq 1 and 3 find X and Y
2X = (S - Sn) + ((S2 - S2n) / (S - Sn))

X = ((S - Sn) + ((S2 - S2n) / (S - Sn))) / 2
Y = X - (S - Sn)
"""

def missingAndRepeatingUsingMaths(arr, n):
    sn = (n*(n+1))//2
    s2n = (n*(n+1)*(2*n+1))//6

    # sum of arr elements
    s = sum(arr)

    # sum of squares of arr elements
    s2 = 0
    for i in range(n):
        s2 += arr[i]*arr[i]

    # Finding repeat and missing using maths
    repeat = ((s-sn) + (s2-s2n)//(s-sn)) // 2
    missing = repeat - (s - sn)
    return (missing, repeat)

"""
OPTIMAL SOL 2:
Refer Striver's video for XOR solution understanding.
TC - O(N)
"""

def missingAndRepeatingUsingXOR(a, n):
    xr = 0

    #Step 1: Find XOR of all elements:
    for i in range(n):
        xr = xr ^ a[i]
        xr = xr ^ (i + 1)

    #Step 2: Find the differentiating bit number:
    number = (xr & ~(xr - 1))

    #Step 3: Group the numbers:
    zero = 0
    one = 0
    for i in range(n):
        #part of 1 group:
        if ((a[i] & number) != 0):
            one = one ^ a[i]
        #part of 0 group:
        else:
            zero = zero ^ a[i]

    for i in range(1, n + 1):
        #part of 1 group:
        if ((i & number) != 0):
            one = one ^ i
        #part of 0 group:
        else:
            zero = zero ^ i

    # Last step: Identify the numbers:
    cnt = 0
    for i in range(n):
        if (a[i] == zero):
            cnt += 1

    if (cnt == 2):
        return (one, zero)
    return (zero, one)



arr = [3, 1, 3, 4, 2]
n = len(arr)
print("The missing and repeating elements are ", missingAndRepeatingUsingMaths(arr, n))
print("The missing and repeating elements are ", missingAndRepeatingUsingXOR(arr, n))
print()
    