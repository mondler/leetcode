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


# %% quicksort; 20211012

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        return self.findKthLargest_inplace(nums, 0, n - 1, k, n)

        # pos_pivot = self.partition(nums, 0, n - 1)
        #
        # if (n - pos_pivot) == k:
        #     return nums[pos_pivot]
        # elif (n - pos_pivot) < k:
        #     return self.findKthLargest(nums[:pos_pivot], k - (n - pos_pivot))
        # else:
        #     return self.findKthLargest(nums[pos_pivot + 1:], k)

    def findKthLargest_inplace(self, nums, left, right, k, n):
        pos_pivot = self.partition(nums, left, right)
        if (n - pos_pivot) == k:
            return nums[pos_pivot]
        elif (n - pos_pivot) < k:
            return self.findKthLargest_inplace(nums, left, pos_pivot - 1, k, n)
        else:
            return self.findKthLargest_inplace(nums, pos_pivot + 1, right, k, n)

    def partition(self, nums, left, right):
        # partition nums from left to right based on a random pivot

        # random pivot to avoid worst case
        import random
        idx_pivot = random.randint(left, right)
        pivot = nums[idx_pivot]
        # print(nums)
        # print(pivot)

        # move pivot to right
        nums[idx_pivot], nums[right] = nums[right], nums[idx_pivot]

        # i is the next position to put number lower than pivot
        i = left
        # scan through nums from left to right, if smaller than pivot, swap to i
        for j in range(left, right + 1):  # last step put pivot in correct place
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # print(nums)
        return i - 1   # position of pivot in nums


nums = [1, 3, 4, 2]

Solution2().findKthLargest(nums, 1)
Solution2().findKthLargest(nums, 2)
Solution2().findKthLargest(nums, 3)
Solution2().findKthLargest(nums, 4)
# Solution().findKthLargest(nums, 2)
# random.randint(1, 10)
