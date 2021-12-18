# 14. Longest Common Prefix
# Easy
#
# 4126
#
# 2231
#
# Add to List
#
# Share
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        res = []

        base = strs[0]

        while len(base) > 0:
            for i, str in enumerate(strs):
                if (len(str) > 0) and (base[0] == str[0]):
                    strs[i] = str[1:]
                else:
                    return "".join(res)

            res.append(base[0])

            base = base[1:]
            # print(strs)
        # print(res)
        return "".join(res)


# %%
# strs = ["flower", "flow", "flight"]
strs = ["ab", "a"]
Solution().longestCommonPrefix(strs)
