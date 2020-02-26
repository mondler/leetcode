# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


class Solution:
    def removeDuplicates1(self, nums):
        """
        96 ms
        :type nums: List[int]
        :rtype: int
        """
        if (lens[sums] == 0):
            return 0
        i = len(nums) - 2
        count = 1
        while (i >= 0):
            if (nums[i] == nums[i + 1]):
                nums.pop(i)
            else:
                count += 1
            i -= 1

        for i in range(count):
            print(nums[i])
        print('done')
        return count

    def removeDuplicates2(self, nums):
        """
        68s
        list.append() has O(1) complexity! also switching is easy
        if an element is not same as before, append to end
        then switch first count elements with last count elements O(count)
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n == 0):
            return 0

        old = nums[0]
        nums.append(old)
        i = 1
        count = 1
        while (i <= (n - 1)):
            current = nums[i]
            if (current == old):
                i += 1
                continue
            else:
                nums.append(current)
                old = current
                count += 1

        for i in range(count):
            nums[i], nums[n + i] = nums[n + i], nums[i]

        return count

    def removeDuplicates(self, nums):
        """
        60ms
        if an element is not same as before
        set nums[count] to be the new value
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0

        count = 1
        old = nums[0]

        for i, num in enumerate(nums):
            if num == old:
                continue
            nums[count] = num
            old = num
            count += 1

        return count


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

nums = []
removeDuplicates(_, nums)

count = 5
nums = nums[-count:]
nums

nums
i = 1
j = 2
nums[i], nums[j] = nums[j], nums[i]

nums

nums[:3 - 1].sort()

nums
