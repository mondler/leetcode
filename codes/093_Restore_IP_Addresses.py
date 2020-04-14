# https://leetcode.com/problems/restore-ip-addresses/description/
# 93. Restore IP Addresses
# Medium
#
# 1032
#
# 460
#
# Add to List
#
# Share
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# Accepted
# 176,544
# Submissions
# 517,275

# %% DFS + Backtracking ~44ms


class Solution(object):
    valid_filed = {str(i) for i in range(256)}

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # s = "25525511135"
        n = len(s)
        if n == 0:
            return []

        ans = set()

        address = ['' for _ in range(4)]

        def DFS(address, i_string, i_field):
            # looking at i_string to fill in i_filed of address
            if i_field == 4:
                if i_string == n:
                    ans.add('.'.join(address))
                return

            for j in range(3):
                if i_string + j + 1 <= n:
                    item = s[i_string:i_string + j + 1]
                    if item in self.valid_filed:
                        address[i_field] = item
                        DFS(address, i_string + j + 1, i_field + 1)

        DFS(address, 0, 0)

        return [item for item in ans]


# %% DFS ~80ms


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # s = "25525511135"
        n = len(s)

        ans = set()

        valid_filed = {str(i) for i in range(256)}

        address = []

        def DFS(address, i):
            # print(address, i)
            if len(address) == 4:
                if i == n:
                    ans.add('.'.join(address))
                return

            for j in range(3):
                # print('here')
                if i + j + 1 <= n:
                    item = s[i:i + j + 1]
                    if item in valid_filed:
                        address.append(item)
                        DFS(address, i + j + 1)
                        del address[-1]

        DFS(address, 0)

        return [item for item in ans]


# %%
s = "010010"
s[4:10]
len(s)
Solution().restoreIpAddresses(s)
