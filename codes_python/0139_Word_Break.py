# 139. Word Break
# Medium
#
# 8835
#
# 404
#
# Add to List
#
# Share
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Accepted
# 938,570
# Submissions
# 2,151,276

# %%
# DP: find if substrings can be broken in segments from wordDict

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def canBreak(s, memory, wordDict):
            if s in memory:
                return memory[s]
            if s in wordDict:
                memory[s] = True
                return True

            for i in range(1, len(s)):
                r = s[i:]
                if r in wordDict and canBreak(s[0:i], memory, wordDict):
                    memory[s] = True
                    print(memory)
                    return True

            memory[s] = False
            return False

        return canBreak(s, {}, wordDict)


# %%

s = "applepenapple"
wordDict = ["apple", "pen"]


print(Solution().wordBreak('applepenapple', wordDict))
