"""
Problem: Min Stack
Platform: LeetCode
Difficulty: Medium
Date: 12-03-2026

Approach:
- Use two stacks:
    1. stack → stores all pushed values.
    2. minstack → keeps track of the minimum value at each step.
- When pushing a new value:
    • Push the value to the main stack.
    • Push the minimum between the current value and the current minimum
      (top of minstack) into minstack.
- When popping:
    • Pop from both stacks to keep them synchronized.
- top() simply returns the last element of the main stack.
- getMin() returns the top of minstack, which always stores the
  minimum value of the stack at that point.

Time Complexity:
- push(): O(1)
- pop(): O(1)
- top(): O(1)
- getMin(): O(1)

Space Complexity: O(n)
- Two stacks are maintained to track elements and minimum values.
"""


class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()