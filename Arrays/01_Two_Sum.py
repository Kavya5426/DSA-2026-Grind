"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy
Date: 23-02-2026

Approach:
- Use a hashmap to store visited elements.
- For each number, calculate complement = target - number.
- If complement exists in hashmap, return indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
