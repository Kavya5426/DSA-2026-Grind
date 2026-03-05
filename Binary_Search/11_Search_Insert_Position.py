"""
Problem: Binary Search
Platform: LeetCode
Difficulty: Easy
Date: 04-03-2026

Approach:
- Use Binary Search to efficiently find the target in a sorted array.
- Maintain two pointers:
    • left → starting index of search space
    • right → ending index of search space
- Repeat while left <= right:
    • Calculate mid index.
    • If nums[mid] equals target, return mid.
    • If target is smaller than nums[mid], search the left half
      by updating right = mid - 1.
    • Otherwise search the right half by updating left = mid + 1.
- If the loop finishes without finding the target,
  return -1.

Time Complexity: O(log n)
- Each iteration halves the search space.

Space Complexity: O(1)
- Only constant extra variables are used.
"""

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 #use '//' in py3 for integer division.'/' gives float result in py3

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1