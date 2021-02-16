#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ordered = OrderedDict(list(enumerate(c)))
    ordered_len = len(ordered)
    current_position = 0
    number_of_jumps = 0
    
    while current_position < ordered_len - 1:
            if current_position != ordered_len - 1:
                if current_position < ordered_len - 2 and ordered[current_position + 2] == 0:
                    current_position += 2
                    number_of_jumps += 1
                elif current_position < ordered_len - 1 and ordered[current_position + 1] == 0:
                    current_position += 1
                    number_of_jumps += 1
                
          
    return number_of_jumps
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

