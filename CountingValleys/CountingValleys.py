



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path

def calculate_position(path):
    position = 0
    poisition_data = [0]
    
    for step in path:
        if step == 'U':
            position += 1
        elif step == 'D':
            position -= 1
        poisition_data.append(position)
        
    return poisition_data

def countingValleys(steps, path):
    in_valley = False
    valley_count = 0
    calculated_position = calculate_position(path)
    
    for i in range(steps):
        print(calculated_position[i])
        if calculated_position[i] == 0 and calculated_position[i+1] == -1:
            in_valley = True
        elif calculated_position[i] == -1 and calculated_position[i+1] == 0 and \
        in_valley:
            valley_count += 1
            in_valley = False            

    return valley_count
        
        
        
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

