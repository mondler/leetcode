# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
#
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
#
# Note that the order of those five elements can be arbitrary.
#
# It doesn't matter what values are set beyond the returned length.


class Solution:
    def removeElement(self, nums, val):
        """
        loop over to check
        if not val, put into front of nums at nums[count]
        """
        if len(nums) == 0:
            return 0
        count = 0
        for num in nums:
            if num == val:
                continue
            nums[count] = num
            count += 1

        return count


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

removeElement(_, nums, val)
nums

nums.remove
