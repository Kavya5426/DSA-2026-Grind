"""
Problem: Sock Merchant
Platform: HackerRank
Difficulty: Easy
Date: 04-03-2026

Approach:
- Use a dictionary (hashmap) to count the frequency of each sock color.
- Traverse the array of socks:
    • For each sock color, increment its count in the dictionary.
- After counting all socks, iterate through the frequency values.
- For each color, the number of pairs is count // 2.
- Sum all pairs and return the result.

Time Complexity: O(n)
- We traverse the array once to count frequencies.
- Then iterate through the dictionary values.

Space Complexity: O(n)
- In the worst case, all socks have different colors,
  so the dictionary stores n elements.
"""
#mount Blue Challenge: 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count={}
    pairs=0
    
    for sock in ar:
        count[sock]=count.get(sock,0)+1
    for p in count.values():
        pairs+=p//2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
