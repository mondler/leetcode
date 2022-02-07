class Solution:

    # Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    #
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    #
    # Example:
    #
    # Given nums = [2, 7, 11, 15], target = 9,
    #
    # Because nums[0] + nums[1] = 2 + 7 = 9,
    # return [0, 1].

    # Best solution in line 161

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = list()
        for i, value in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if ((value + nums[j]) == target):
                    idx.append(i)
                    idx.append(j)

        return idx

    def twoSum2(self, nums, target):
        """
        sort nums and retain order in original list
        start with a[0], check a[0]+a[1], then a[0]+a[n-1]
        then move to middle

        SHOULD consider check middle first
        """
        idx = list()
        order = sorted(range(len(nums)), key=lambda k: nums[k])
        nums = [nums[i] for i in order]

        for i, value in enumerate(nums):
            i0 = i + 1
            i1 = len(nums) - 1
            while (i0 <= i1):
                if ((value + nums[i0]) == target):
                    idx.append(i)
                    idx.append(i0)
                    ans = [order[i] for i in idx]
                    ans.sort()
                    return ans
                elif ((value + nums[i0]) > target):
                    break
                elif (i1 > i0):  # ((value + nums[i0]) < target)
                    if ((value + nums[i1]) == target):
                        idx.append(i)
                        idx.append(i1)
                        ans = [order[i] for i in idx]
                        ans.sort()
                        return ans
                    elif ((value + nums[i1]) < target):
                        break
                    else:
                        i0 += 1
                        i1 -= 1
                else:
                    break

        return idx

    def twoSum3(self, nums, target):
        """
        sort nums and retain order in original list
        start with a[0], check a[0]+a[n/2]
        """
        n = len(nums)
        order = sorted(range(n), key=lambda k: nums[k])
        nums = [nums[i] for i in order]

        def checkTarget(i, j):
            """
            check if ith and jth add up to target
            return +1 if i+j > target
            return  0 if i+j = target
            return -1 if i+j < target
            """
            ans = nums[i] + nums[j] - target
            return ((ans > 0) - (ans < 0))  # sign of ans

        # def myRound(i0, i1):
        #     """
        #     ceil of (i0+i1)/2
        #     """
        #     a = i0 + i1
        #     if divmod(a, 2)[1] == 0:
        #         return int(a * 0.5)
        #     else:
        #         return int(a * 0.5 - 0.5)

        for i in range(n):
            # print('i is', i)
            # initiate values
            i0 = i + 1
            i1 = n - 1

            while (i0 <= i1):
                # print('middle is ', middle)

                # middle = myRound(i0, i1)
                middle = round((i0 + i1) * 0.5)

                check = checkTarget(i, middle)
                # print('check is ', check)

                if check == 0:
                    ans = [order[j] for j in [i, middle]]
                    ans.sort()
                    return ans
                elif check > 0:
                    i1 = middle - 1
                else:
                    i0 = middle + 1

    def twoSum4(self, nums, target):
        """
        sort nums and retain order in original list
        start with a[0] + a[n-1],
        then shrink to middle

        THIS is actually slower than twoSum3
        """
        n = len(nums)
        order = sorted(range(n), key=lambda k: nums[k])
        nums = [nums[i] for i in order]

        def checkTarget(i, j):
            """
            check if ith and jth add up to target
            return +1 if i+j > target
            return  0 if i+j = target
            return -1 if i+j < target
            """
            ans = nums[i] + nums[j] - target
            return ((ans > 0) - (ans < 0))  # sign of ans

        i0 = 0
        i1 = n - 1

        while (i0 <= i1):
            check = checkTarget(i0, i1)
            if check == 0:
                ans = [order[i] for i in [i0, i1]]
                ans.sort()
                return ans
            elif check > 0:
                i1 -= 1
            else:
                i0 += 1

    def twoSum(self, nums, target):
        """
        Solution based on leetcode discussion
        Using dictionary to store each input's index and num
        Search new num's complement in dictinary, if not, store {num: index}
        """
        dict = {}  # {num: index of num in nums}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [dict[complement], i]
            else:
                dict[num] = i  # store index of num in dict

    # nums = [2, 7, 11, 9]
    nums = [2, 5, 5, 11]
    target = 10

    nums = [5, 5]
    target = 10

    nums = [-10, -1, -18, -19]
    target = -37

    twoSum(_, nums, target)

    twoSum(_, nums, target)
    twoSum2(_, nums, target)


dic = {1: 2}

1 in dic

dic['a'] = 3

dic

dic[3] = 9
