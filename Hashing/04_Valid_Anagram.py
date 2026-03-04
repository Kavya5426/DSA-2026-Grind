"""
Problem: Valid Anagram
Platform: LeetCode
Difficulty: Easy
Date: 24-02-2026

Approach:
- First check if lengths of both strings are equal.
- If not equal, they cannot be anagrams.
- Use a dictionary to count frequency of characters in string s.
- Traverse string t:
    • If character is not in dictionary, return False.
    • Decrement its frequency.
    • If frequency becomes negative, return False.
- If all checks pass, return True.

Time Complexity: O(n)
- Both strings are traversed once.

Space Complexity: O(1)
- Since only lowercase English letters are used,
  the dictionary size is bounded (maximum 26 characters).
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
            return False
        
        count={}

        for char in s:
            count[char]=count.get(char,0)+1

        for char in t:
            if char not in count:
                return False
            count[char]-=1
            if count[char]< 0:
                return False
        return True