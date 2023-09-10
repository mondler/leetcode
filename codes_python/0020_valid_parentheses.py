#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.20%)
# Likes:    21879
# Dislikes: 1444
# Total Accepted:    3.7M
# Total Submissions: 9.3M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#
# %%
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        unmatched = []
        for p in s:
            if len(unmatched) == 0:
                unmatched.append(p)
            elif self.is_match(unmatched[-1], p):
                unmatched.pop()
            else:
                unmatched.append(p)
        return len(unmatched) == 0
    
    @classmethod
    def is_match(cls, frist, second) -> bool:
        if frist == "(" and second == ")":
            return True
        elif frist == "[" and second == "]":
            return True
        elif frist == "{" and second == "}":
            return True
        else:
            return False
        
        
# @lc code=end
solution = Solution()
s1 = "()[]{}"
print(solution.isValid(s1))
s2 = "(}"
print(solution.isValid(s2))

# print(solution.is_match(')', '('))
# print(solution.is_match(')', '{'))



# %%
