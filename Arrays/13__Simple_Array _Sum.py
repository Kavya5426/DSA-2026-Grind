"""
Problem: Simple Array Sum
Platform: HackerRank (MoonBlue Challenge)
Difficulty: Easy
Date: 05-03-2026

Approach:
- Initialize a variable `total` to store the sum.
- Traverse the array and add each element to `total`.
- Return the final sum.

Time Complexity: O(n)
- Each element of the array is visited once.

Space Complexity: O(1)
- No extra space is used besides the variable `total`.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    total=0;
    for i in range(len(ar)):
                   total+=ar[i]
    return total;
                 
                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()