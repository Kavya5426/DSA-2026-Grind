"""
Problem: Valid Parentheses
Platform: LeetCode
Difficulty: Easy
Date: 12-03-2026

Approach:
- Use a stack to track opening brackets.
- Traverse the string character by character.
- If the character is an opening bracket '(', '{', or '[', push it onto the stack.
- If it is a closing bracket, check the top of the stack:
    • If the stack is empty, the parentheses are invalid.
    • Pop the top element and verify it matches the corresponding opening bracket.
- If at any point the brackets do not match, return False.
- After processing the entire string, the stack should be empty for the parentheses to be valid.

Time Complexity: O(n)
- Each character in the string is processed once.

Space Complexity: O(n)
- In the worst case, all characters may be opening brackets stored in the stack.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if ch==')' and top!='(':
                    return False
                if ch=='}' and top!='{':
                    return False
                if ch==']' and top!='[':
                    return False
        return not stack
    
    
    
    """
Problem: Valid Parentheses
Platform: LeetCode
Difficulty: Easy
Date: 12-03-2026

Approach:
- Use a stack to keep track of opening brackets.
- Create a dictionary that maps closing brackets to their corresponding opening brackets.
- Traverse the string character by character.
- If the character is an opening bracket, push it onto the stack.
- If the character is a closing bracket:
    • Check if the stack is empty or the top of the stack does not match the required opening bracket.
    • If so, return False.
    • Otherwise, pop the top element from the stack.
- After processing all characters, the stack should be empty for the string to be valid.

Time Complexity: O(n)
- Each character in the string is processed once.

Space Complexity: O(n)
- In the worst case, all characters may be opening brackets stored in the stack.
"""
    
    
    class Solution(object):
        def isValid(self, s):

            stack = []

            mapping = {
                ')': '(',
                ']': '[',
                '}': '{'
            }

            for char in s:

                if char in mapping:
                    if not stack or stack[-1] != mapping[char]:
                        return False
                    stack.pop()

                else:
                    stack.append(char)

            return len(stack) == 0