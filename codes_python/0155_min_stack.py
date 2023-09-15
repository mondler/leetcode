#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Medium (52.92%)
# Likes:    12875
# Dislikes: 783
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
# '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# Implement the MinStack class:
#
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
#
#
# You must implement a solution with O(1) time complexity for each function.
#
#
# Example 1:
#
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
#
#
# Constraints:
#
#
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
#
#
#
# %%
# @lc code=start
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        return

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not(self.min_stack):
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
        return

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# @lc code=end

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.stack)
print(obj.top())
print(obj.getMin())
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
