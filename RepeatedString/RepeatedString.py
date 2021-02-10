#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_frequency = 0
    length_s = len(s)
    a_positions = list(filter(lambda x: x[1] == 'a', enumerate(s)))
    
    if bool(a_positions) is False:
        return 0
    else:
        for position, _ in a_positions:
            a_frequency += math.ceil((n - position) / length_s)
    
    return a_frequency
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

