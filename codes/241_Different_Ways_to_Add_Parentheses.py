# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
# 241. Different Ways to Add Parentheses
# Medium
#
# 1364
#
# 68
#
# Add to List
#
# Share
# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Accepted
# 92,133
# Submissions
# 172,670

# %% seperate by operator, divide and counter


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        m_ = {}  # save results of earlier calculation

        def ways(input):
            if input in m_:  # pull results if already calculated
                return m_[input]

            cal = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
            }

            ans = []
            for i, c in enumerate(input):
                if c in ['+', '-', '*']:
                    l = ways(input[:i])
                    r = ways(input[i + 1:])
                    for a in l:
                        for b in r:
                            ans.append(cal[c](a, b))
            # null case
            if not(ans):  # if input is single number without operator
                ans = [int(input)]

            m_[input] = ans
            return ans

        return ways(input)


# %%

input = '2*3-4*5'
Solution().diffWaysToCompute(input)
