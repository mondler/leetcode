# 350. Intersection of Two Arrays II
# Easy
#
# 2211
#
# 525
#
# Add to List
#
# Share
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
#
#
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# %% 1st solution using counts for both nums

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # count freq using dict
        def countToDict(nums: list[int]) -> dict():
            counts = dict()
            for i in nums:
                counts[i] = counts.get(i, 0) + 1
            return counts

        res = []

        ct1, ct2 = countToDict(nums1), countToDict(nums2)

        for k in ct2:
            while (ct2.get(k, 0) > 0) and (ct1.get(k, 0) > 0):
                # print('here')
                res.append(k)
                ct2[k] -= 1
                ct1[k] -= 1

        return res

# %% 2nd solution using counts for nums1 only


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # count freq using dict
        ct1 = dict()
        for i in nums1:
            ct1[i] = ct1.get(i, 0) + 1

        res = []

        for n in nums2:
            if ct1.get(n, 0) > 0:
                res.append(n)
                ct1[n] -= 1

        return res


# %%
nums1 = [9, 9, 4]
# nums2 = [9]
nums2 = [9, 4, 9, 8, 4]
Solution().intersect(nums1, nums2)


# %% extension: if both nums are sorted


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        res = []

        i, j = 0, 0

        m, n = len(nums1), len(nums2)

        while (i < m) and (j < n):
            n1 = nums1[i]
            n2 = nums2[j]
            # print(i, j)
            if n1 == n2:
                res.append(n1)
                i += 1
                j += 1
            elif n1 < n2:
                i += 1
            else:
                j += 1

        return res


# %%
nums1 = []
# nums2 = [9]
nums2 = [2, 3, 4]
Solution().intersect(nums1, nums2)
