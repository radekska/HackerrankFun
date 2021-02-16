#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    set_of_sum = set()
    len_of_row = len(arr)
    len_of_col = len(arr[0])
    
    for n in range(len_of_row):
        for m in range(len_of_col):
            if n <= len_of_row - 3 and m <= len_of_row - 3:
                hourglass_sum = sum(arr[n][m:m+3]) + arr[n+1][m+1] + sum(arr[n+2][m:m+3])
                set_of_sum.add(hourglass_sum)
              
    return max(set_of_sum)
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

