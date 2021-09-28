# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# 524. Longest Word in Dictionary through Deleting
# Medium
#
# 448
#
# 204
#
# Add to List
#
# Share
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
#
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
#
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
#
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


# %% use python function s.find(l, i) to find if l (letter of w) is in s
# fastest

class Solution(object):
    def findLongestWord(self, s, d):
        def helper(w, s):
            i = 0
            for l in w:
                i = s.find(l, i) + 1  # s.find returns -1 if not found
                if not i:  # if i == 0
                    return False
            return True
        # d.sort(key=lambda x: (-len(x), x))
        # for w in d:
        #     if helper(w, s):
        #         return w
        # return ""

        shortlist = [w for w in d if helper(w, s)]
        if len(shortlist) == 0:
            return ""
        shortlist.sort(key=lambda x: (-len(x), x))
        return shortlist[0]


# %% Initial Solution, find letter, find word, sort word
# same speed as two pointer, find first and sort later

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        shortlist = [w for w in d if self.findWord(s, w)]
        if len(shortlist) == 0:
            return ''
        shortlist.sort(key=lambda w: (-len(w), w))
        return shortlist[0]

    def findWord(self, s, w):
        # find if w can be found in s by deleting letters
        # try:
        #     len_s = len(s)
        #     if len_s == 0:
        #         return False
        # except:
        #     return False
        loc = 0  # location in string to start looking
        for l in w:
            loc = self.findLetter(s, l, loc) + 1
            if loc == 0:
                return False
        return True

    def findLetter(self, s, l, loc):
        # find l in s starting from s[loc]
        # return location of l in s
        # return -1 if not found
        len_s = len(s)
        while loc < len_s:
            if s[loc] == l:
                return loc
            loc += 1
        return -1


# %%
w = 'apple'
l = 'a'
loc = 2
d = ['bp', 'apple', 'pcple', 'ple', 'cat']
s = 'abpcplea'
Solution().findLetter(s, l, 0)
# Solution().findWord(s, w)
# s = "abpcplea"
# d = ["a","b","c"]
# Solution().findLongestWord(s, d)


# %% two pointer; sort first; find later


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda w: (-len(w), w))
        for w in d:
            i = 0
            for l in s:
                if i < len(w) and w[i] == l:
                    i += 1
            if i == len(w):
                return w
        return ""


# %% two pointer; find first, sort later

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        shortlist = []

        for w in d:
            i = 0
            for l in s:
                if i < len(w) and w[i] == l:
                    i += 1
            if i == len(w):
                shortlist.append(w)
        if len(shortlist) == 0:
            return ""
        shortlist.sort(key=lambda w: (-len(w), w))
        return shortlist[0]


# %%
w = 'apple'
l = 'a'
loc = 2
d = ['bp', 'apple', 'pcple', 'ple', 'cat']
s = 'abpcplea'
# Solution.findLetter(s, l, loc)
# Solution().findWord(s, w)
# s = "abpcplea"
# d = ["a","b","c"]
Solution().findLongestWord(s, d)
