"""
Problem: Search Insert Position
Platform: LeetCode
Difficulty: Easy
Date: 12-03-2026

Approach:
- The array is sorted, so we can apply Binary Search.
- Initialize two pointers: left at the beginning and right at the end of the array.
- Calculate the middle index in each iteration.
- If the middle element equals the target, return its index.
- If the target is greater than the middle element, move the left pointer to mid + 1.
- If the target is smaller than the middle element, move the right pointer to mid - 1.
- If the target is not found, the loop ends when left surpasses right.
- At that point, the left pointer indicates the correct position where the target
  should be inserted to maintain sorted order.

Time Complexity: O(log n)
- Binary search halves the search space in each iteration.

Space Complexity: O(1)
- Only constant extra space is used.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left