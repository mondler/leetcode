# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


# %%


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        newSum = maxSum
        for n in nums[1:]:
            if newSum > 0:  # keep previous sum if it is larger than zero
                newSum = newSum + n
            else:
                newSum = n
            maxSum = max(newSum, maxSum)  # record current max
        return maxSum


# %%


class Solution:
    def maxSubArray(self, nums):
        """
        loop over all number
        96ms
        """
        currentSum = nums[0]
        newSum = 0
        for num in nums:
            newSum += num
            # print('new sum is {}'.format(newSum))
            if newSum > currentSum:
                currentSum = newSum
            if newSum < 0:
                newSum = 0

        return currentSum


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def divide_and_conquer(nums, i, j):
            if i == j - 1:
                return nums[i], nums[i], nums[i], nums[i]

            # we will compute :
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]

            # compute middle index to divide array in two halves
            i_mid = i + (j - i) // 2

            # compute a, m, b, s for left half
            a1, m1, b1, s1 = divide_and_conquer(nums, i, i_mid)

            # compute a, m, b, s for right half
            a2, m2, b2, s2 = divide_and_conquer(nums, i_mid, j)

            # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
            a = max(a1, s1 + a2)
            b = max(b2, s2 + b1)
            m = max(m1, m2, b1 + a2)
            s = s1 + s2
            return a, m, b, s

        _, m, _, _ = divide_and_conquer(nums, 0, len(nums))
        return m

    # def maxSubArray(self, nums):
    #     """
    #     Divided and conquer algorithm
    #     Based on Introduction to algorithms, chapter 4.1
    #     """
    #     def find_max_crossing_subarray(nums, low, mid, high):
    #         import math
    #         left_sum = -math.inf
    #         s = 0
    #         i = mid
    #         while i >= low:
    #             s += nums[i]
    #             if s > left_sum:
    #                 left_sum = s
    #                 max_left = i
    #             i -= 1
    #
    #         right_sum = -math.inf
    #         s = 0
    #         i = mid + 1
    #         while i <= high:
    #             s += nums[i]
    #             if s > right_sum:
    #                 right_sum = s
    #                 max_right = i
    #             i += 1
    #
    #         return left_sum + right_sum, max_left, max_right
    #
    #     def find_max_subarray(nums, low, high):
    #         # print('\n')
    #         # print('low is ', low)
    #         # print('high is ', high)
    #         if low - high == 0:
    #             return (nums[low], low, high)
    #         else:
    #             mid = (low + high) // 2
    #             # print('mid is ', mid)
    #             left_sum, left_low, left_high = find_max_subarray(
    #                 nums, low, mid)
    #             print('left_sum', left_sum)
    #             right_sum, right_low, right_high = find_max_subarray(
    #                 nums, mid + 1, high)
    #             print('right_sum', right_sum)
    #             cross_sum, cross_low, cross_high = find_max_crossing_subarray(
    #                 nums, low, mid, high)
    #             print('cross_sum', cross_sum)
    #
    #             if left_sum >= right_sum:
    #                 print('surprise')
    #
    #             if (left_sum >= right_sum) & (left_sum >= cross_sum):
    #                 # print('choose left')
    #                 # print('left_sum', left_sum)
    #                 # print('right_sum', right_sum)
    #                 return left_sum, left_low, left_high
    #             elif (right_sum >= left_sum) & (right_sum >= cross_sum):
    #                 # print('choose left')
    #                 return right_sum, right_low, right_high
    #             else:
    #                 print('choose cross')
    #                 return cross_sum, cross_low, cross_high
    #
    #     (max_sum, left, right) = find_max_subarray(nums, 0, len(nums) - 1)
    #     return max_sum


nums = [-2, -1]
Solution().maxSubArray(nums)
