"""
Problem: Kangaroo
Platform: HackerRank
Difficulty: Easy
Date: 08-03-2026

Approach:
- Two kangaroos start at positions x1 and x2 with jump velocities v1 and v2.
- After k jumps their positions will be:
    kangaroo1 = x1 + k * v1
    kangaroo2 = x2 + k * v2
- We check if there exists an integer k such that both positions become equal.

Equation:
    x1 + k*v1 = x2 + k*v2

Rearranging:
    k = (x2 - x1) / (v1 - v2)

Conditions:
1. If v1 <= v2 and x1 < x2, the first kangaroo will never catch up → return "NO".
2. If (x2 - x1) is divisible by (v1 - v2), then both kangaroos land at the same position → return "YES".
3. Otherwise → return "NO".

Time Complexity: O(1)
- Only constant time mathematical operations are used.

Space Complexity: O(1)
- No additional data structures are used.
"""
#mount Blue Challenge: 4

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1 <= v2:
        return "NO"
    if(x2-x1)%(v1-v2)==0:
        return "YES"
    else:
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()