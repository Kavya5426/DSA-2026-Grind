"""
Problem: Two Sum
Platform: LeetCode
Difficulty: Easy
Date: 23-02-2026

Approach:
- Iterate through the array using two nested loops.
- For each element nums[i], check every element after it nums[j].
- If nums[i] + nums[j] equals the target, return their indices.
- This ensures all possible pairs are checked.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return (i,j);
        

        
