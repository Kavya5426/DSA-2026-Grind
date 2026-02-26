"""
Problem: Move Zeroes
Platform: LeetCode
Difficulty: Easy
Date: 27-02-2026

Approach:
- Use a pointer `ins_pos` to track the position where the next non-zero element should be placed.
- Traverse the array once:
    • If the current element is non-zero, place it at index `ins_pos`.
    • Increment `ins_pos`.
- After moving all non-zero elements to the front,
  fill the remaining positions in the array with zeros.
- This modifies the array in-place without using extra space.

Time Complexity: O(n)
- The array is traversed twice (which is still linear time).

Space Complexity: O(1)
- No extra data structures are used.
- Modification is done in-place.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ins_pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[ins_pos]=nums[i]
                ins_pos+=1
        for i in range(ins_pos,len(nums)):
            nums[i]=0;