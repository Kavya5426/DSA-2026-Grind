"""
Problem: Breaking the Records
Platform: HackerRank
Difficulty: Easy
Date: 08-03-2026

Approach:
- Initialize two variables to track the highest score and lowest score.
- The first score is considered both the initial maximum and minimum.
- Traverse the scores list starting from the second element.
- For each score:
    • If it is greater than the current maximum score, update the maximum
      and increment the max record break counter.
    • If it is lower than the current minimum score, update the minimum
      and increment the min record break counter.
- Return the number of times the maximum and minimum records were broken.

Time Complexity: O(n)
- The list is traversed once.

Space Complexity: O(1)
- Only constant extra variables are used to track scores and counts.
"""
#Mount Blue Challenge: 3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxscore=scores[0]
    minscore=scores[0]
    res=[0,0]
    for i in range(1,len(scores)):
        if scores[i]>maxscore:
            maxscore=scores[i]
            res[0]=res[0]+1
        elif scores[i]<minscore:
            minscore=scores[i]
            res[1]=res[1]+1
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()