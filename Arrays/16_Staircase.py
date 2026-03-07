"""
Problem: Staircase
Platform: HackerRank
Difficulty: Easy
Date: 08-03-2026

Approach:
- The goal is to print a right-aligned staircase of height n using '#' symbols.
- For each row i (from 1 to n):
    • Print (n - i) spaces.
    • Print i '#' characters.
- Combining spaces and '#' ensures the staircase is right-aligned.

Example for n = 4:

   #
  ##
 ###
####

Time Complexity: O(n²)
- The loop runs n times.
- In each iteration, up to n characters are printed.

Space Complexity: O(1)
- No additional data structures are used.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#mount Blue Challenge: 5

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*(i))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)