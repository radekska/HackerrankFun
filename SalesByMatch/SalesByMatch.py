#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counted_socks = Counter(ar)
    pairs = 0
    for number in counted_socks.values():
        pairs += (number // 2)
    return pairs
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
