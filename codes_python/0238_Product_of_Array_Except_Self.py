# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Accepted
# 1.9M
# Submissions
# 2.9M
# Acceptance Rate
# 65.0%


# %%
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        res = [1] * n
        for i in range(1, n):
            # product of nums before nums[i]
            pre[i] = pre[i - 1] * nums[i - 1]
            # product of nums after nums[n-i-1]
            post[n - i - 1] = post[n - i] * nums[n - i]
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res


# %%
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))
