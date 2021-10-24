# 611. Valid Triangle Number
# Medium
#
# 2074
#
# 134
#
# Add to List
#
# Share
# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
#
#
#
# Example 1:
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Example 2:
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# Accepted
# 119,606
# Submissions
# 243,331

# %%

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        # nums = [4, 3, 1, 2]

        res = 0

        l = len(nums)
        if l < 3:
            return res

        nums.sort(reverse=True)

        # a <= b <= c, need a + b > c
        for loc_c, c in enumerate(nums):
            # for loc_b in range(loc_c + 1, l - 1):
            loc_b = loc_c + 1
            loc_a = l - 1
            while (loc_b < loc_a):
                b = nums[loc_b]
                a = nums[loc_a]
                if (a + b > c):
                    res += loc_a - loc_b
                    loc_b += 1
                else:
                    loc_a -= 1

        return res


# %%
nums = [2, 2, 3, 4]
print(Solution().triangleNumber(nums))

nums = [4, 2, 3, 4]
print(Solution().triangleNumber(nums))

nums = [20, 10, 3, 2, 1]
print(Solution().triangleNumber(nums))
