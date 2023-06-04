from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] =  matrix[0][j] = 0
    
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == 0:
            matrix[i][0] = 0
                              
    return matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter elements one by one: ")
matrix = [[int(input()) for x in range (cols)] for y in range(rows)]  
print("Matrix Before: ")
print(matrix)
setZeros(matrix)
print("Matrix After: ")
print(matrix)