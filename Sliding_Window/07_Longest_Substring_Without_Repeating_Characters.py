"""
Problem: Longest Substring Without Repeating Characters
Platform: LeetCode
Difficulty: Medium
Date: 28-02-2026

Approach:
- Use the Sliding Window technique with two pointers.
- Maintain a set `seen` to store characters in the current window.
- Use two pointers:
    • i → right pointer (expands window)
    • j → left pointer (shrinks window when duplicate found)
- Traverse the string:
    • If s[i] is already in the set, shrink the window
      by removing characters from the left (increment j)
      until duplicate is removed.
    • Add s[i] to the set.
    • Update max_len as the maximum window size (i - j + 1).
- Return max_len at the end.

Time Complexity: O(n)
- Each character is added and removed from the set at most once.
- Both pointers traverse the string at most n times.

Space Complexity: O(min(n, m))
- Where n = length of string,
  m = size of character set.
- In worst case, all characters are unique and stored in the set.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        max_len=0
        j=0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j+=1
            seen.add(s[i])
            max_len=max(max_len,i-j + 1)
        return max_len

            
        