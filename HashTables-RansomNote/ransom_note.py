#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def checkMagazine(magazine, note):
    magazine_counted = Counter(magazine)
    note_counted = Counter(note)

    for word, count in magazine_counted.items():
        if note_counted.get(word, None):
            note_counted[word] -= count

    note_remaining = list(filter(lambda count: count > 0, note_counted.values()))

    if not any(note_remaining):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

