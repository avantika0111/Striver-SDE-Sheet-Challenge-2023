def generateRow(n):
    res = [1]
    ans = 1
    for i in range(1, n):
        ans = ans*(n-i)
        ans = ans // i
        res.append(ans)
    return res

n = int(input("Enter number of rows: "))
triangle = []
for i in range(n):
    triangle.append(generateRow(i+1))
print("Pascal's Triangle is : ")
print(triangle)