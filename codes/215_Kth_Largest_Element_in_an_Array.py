# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# 215. Kth Largest Element in an Array
# Medium
#
# 2932
#
# 208
#
# Add to List
#
# Share
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


# %% Quickselect/Quicksort

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # let's do quick selection, change k to 0-based

        def quickSelect(start, end, k):
            if start == end:
                return nums[start]

            pivot = random.randint(start, end)
            nums[end], nums[pivot] = nums[pivot], nums[end]
            #print(start, end, k)
            j = start
            for i in range(start, end):
                if nums[i] > nums[end]:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            nums[j], nums[end] = nums[end], nums[j]
            #print(pivot, j, nums)

            if j == k:
                return nums[j]
            elif j > k:
                return quickSelect(start, j - 1, k)
            else:
                return quickSelect(j + 1, end, k)

        return quickSelect(0, len(nums) - 1, k - 1)


# %% This also works if pivot is randomly assigned


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        loc_for_pivot = self.partition(nums, 0, n - 1)
        loc_from_right = n - loc_for_pivot
        if loc_from_right == k:
            return nums[-k]
        elif loc_from_right > k:
            # if target on the right
            # pass in the right part, k remains
            return self.findKthLargest(nums[loc_for_pivot + 1:], k)
        else:
            # if target on the left
            # pass in the left, revise k
            return self.findKthLargest(nums[:loc_for_pivot], k - loc_from_right)

    def partition(self, nums, left, right):
        # left: starting index
        # right: end index
        # need random pivot instead of end
        import random
        pivot = random.randint(left, right)
        nums[end], nums[pivot] = nums[pivot], nums[end]
        loc_for_low, i = 0, 0
        pivot = nums[right]
        # while i < right:
        #     if nums[i] < pivot:  # put smaller than pivot value to front of the list
        #         nums[i], nums[loc_for_low] = nums[loc_for_low], nums[i]
        #         loc_for_low += 1
        #     i += 1
        for i, n in enumerate(nums):
            if n < pivot:
                nums[i], nums[loc_for_low] = nums[loc_for_low], nums[i]
                loc_for_low += 1
        if loc_for_low < right:
            nums[right], nums[loc_for_low] = nums[loc_for_low], nums[right]
        return loc_for_low  # index of pivot


# %%

nums = [80, 80, 60, 70]
# Solution().partition(nums, 0, 3)
Solution().findKthLargest(nums, 2)
random.randint(1, 10)
