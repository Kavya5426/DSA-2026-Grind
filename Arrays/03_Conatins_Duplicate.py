"""
Problem: Contains Duplicate
Platform: LeetCode
Difficulty: Easy
Date: 24-02-2026

Approach:
- Initialize an empty set to track seen elements.
- Traverse the array.
- For each number:
    • If it already exists in the set, return True.
    • Otherwise, add it to the set.
- If traversal completes without finding duplicates, return False.

Time Complexity: O(n)
- Each element is processed once.
- Set lookup and insertion are O(1) on average.

Space Complexity: O(n)
- In the worst case, all elements are unique and stored in the set.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        