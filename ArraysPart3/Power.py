'''
TC - O(logN)
'''
def power(x, n):
    res = 1
    if n < 0:
        n = -1 * n
    while n > 0:
        if n % 2 == 0:
            x *= x
            n = n // 2
        else:
            res *= x 
            n = n - 1
    if n < 0:
        res = 1 / res
    return res

if __name__ == "__main__":
    print(power(2, 10))