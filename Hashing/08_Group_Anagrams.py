"""
Problem: Group Anagrams
Platform: LeetCode
Difficulty: Medium
Date: 29-02-2026

Approach:
- Use a dictionary to group words that are anagrams.
- For each word in the input list:
    • Sort the characters of the word.
    • Use the sorted string as a key in the dictionary.
- Since anagrams have the same characters in different order,
  sorting them produces the same key.
- Append the original word to the list corresponding to that key.
- Finally, return all grouped values from the dictionary.

Time Complexity: O(n * k log k)
- n = number of words
- k = maximum length of a word
- Sorting each word takes O(k log k)
- Done for all n words

Space Complexity: O(n * k)
- Dictionary stores all words.
- Sorted keys also require space.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word not in grp:
                grp[sorted_word]=[]

            grp[sorted_word].append(word)
        return list(grp.values())