#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    len_of_arr = len(arr)
    minimal_diff = max(arr)
    for i in range(len_of_arr):
        if i < len_of_arr - 1:
            current_diff = abs(sorted_arr[i] - sorted_arr[i+1])
            if current_diff < minimal_diff:
                minimal_diff = current_diff
                
    return minimal_diff

 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

