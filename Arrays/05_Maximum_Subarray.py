"""
Problem: Maximum Subarray
Platform: LeetCode
Difficulty: Medium
Date: 26-02-2026

Approach:
- Use Kadane’s Algorithm to find the maximum sum of a contiguous subarray.
- Maintain a variable current_sum to track the running subarray sum.
- Traverse the array:
    • Add current element to current_sum.
    • Update maxsum if current_sum is greater.
    • If current_sum becomes negative, reset it to 0
      because a negative sum will reduce future subarray sums.
- Return maxsum at the end.

Time Complexity: O(n)
- The array is traversed once.

Space Complexity: O(1)
- Only constant variables are used (current_sum and maxsum).
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        maxsum = float('-inf')

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum > maxsum:
                maxsum = current_sum

            if current_sum < 0:
                current_sum = 0

        return maxsum
