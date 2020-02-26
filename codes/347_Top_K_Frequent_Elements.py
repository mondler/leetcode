# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# 347. Top K Frequent Elements
# Medium
#
# 2355
#
# 156
#
# Add to List
#
# Share
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# Accepted
# 311,893
# Submissions
# 530,185


# %% count freq, sort, output; this is faster than below

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(nums).most_common()
        topK = []
        for i in range(k):
            topK.append(count[i][0])
        return topK

# %% defaultdict; cnt as key, nums as values; output


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict, Counter
        frq = defaultdict(list)
        for num, cnt in Counter(nums).items():
            frq[cnt].append(num)

        res = []
        for cnt in range(len(nums), 0, -1):
            res.extend(frq[cnt])
            if len(res) >= k:
                break
        return res[:k]


# %%
nums = [1, 10, 10, 10, 5, 5, 3]
k = 2
Solution().topKFrequent(nums, k)
