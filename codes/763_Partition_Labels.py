# https://leetcode.com/problems/partition-labels/description/
# 763. Partition Labels
# Medium
#
# 1636
#
# 78
#
# Add to List
#
# Share
# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# Accepted
# 90,195
# Submissions
# 122,591


# %%

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        pos_right = {}
        # for i, c in enumerate(S):
        #     pos_right[c] = i
        for i, c in enumerate(S[::-1]):
            if c not in pos_right:
                pos_right[c] = n - i - 1
        partition_size = []
        curr_left = 0
        # first part need to extend at least to curr_right
        curr_right = pos_right[S[0]]
        for i, c in enumerate(S):
            if i == curr_right:  # if successfully reaching curr_right
                partition_size.append(curr_right - curr_left + 1)
                if i < n - 1:
                    curr_left = i + 1
                    curr_right = pos_right[S[i + 1]]
            elif pos_right[c] > curr_right:  # else, extend even more
                curr_right = pos_right[c]
        return partition_size


# %%
S = "ababcbacadefegdehijhklij"
Solution().partitionLabels(S)
S = "abca"
Solution().partitionLabels(S)
S = "aabacdc"
Solution().partitionLabels(S)
