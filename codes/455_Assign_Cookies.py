# https://leetcode.com/problems/assign-cookies/description/
#
# 455. Assign Cookies
# Easy
#
# 460
#
# 80
#
# Add to List
#
# Share
# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
#
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.
#
# Example 1:
#
# Input: [1,2,3], [1,1]
#
# Output: 1
#
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:
#
# Input: [1,2], [1,2,3]
#
# Output: 2
#
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.
# Accepted
# 82,737
# Submissions
# 168,385


# %%

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        count = 0  # number of content child
        i = 0  # index for child
        j = 0  # index for cookie
        m = len(s)  # length/number of cookie
        n = len(g)  # number of child
        while j < m:
            if s[j] >= g[i]:
                count += 1
                i += 1
                if i >= n:  # every child satisfied
                    return n
            j += 1
        return count

 # %%


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g, reverse=True)  # lowest greedy child put to end
        s = sorted(s)

        count = 0
        for sj in s:
            if sj >= g[-1]:
                g.pop()
                count += 1
            if not g:
                return count
        return count



# %%
g, s = [1, 2], [1, 2, 3]
Solution().findContentChildren(g, s)

g, s = [1, 2, 3], [1, 1]
Solution().findContentChildren(g, s)
