"""
Problem: Valid Palindrome
Platform: LeetCode
Difficulty: Easy
Date: 01-03-2026

Approach:
- Create a new string `clean` to store only alphanumeric characters.
- Traverse the input string:
    • If a character is alphanumeric, convert it to lowercase
      and append it to `clean`.
- After cleaning the string, compare it with its reverse.
- If both are equal, the string is a palindrome.
- Otherwise, return False.

Time Complexity: O(n)
- We traverse the string once to clean it.
- Reversing the string also takes O(n).
- Overall complexity remains linear.

Space Complexity: O(n)
- A new string `clean` is created to store filtered characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean=""
        for char in s:
            if char.isalnum():
                clean+=char.lower()
        return clean==clean[::-1]
    
#Space complexity can be optimized to O(1) by using two pointers instead of creating a new string.
    
        