# https://leetcode.com/problems/can-place-flowers/description/
# 605. Can Place Flowers
# Easy
#
# 647
#
# 324
#
# Add to List
#
# Share
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
#
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.


# %%
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        length = len(flowerbed)
        cnt = 0
        i = 0
        while i < length:
            if flowerbed[i] == 1:
                i += 2  # if flower, savely jump to i + 2
                continue
            pre_clear = (i == 0) or (flowerbed[i - 1] == 0)
            post_clear = (i == length - 1) or (flowerbed[i + 1] == 0)
            if pre_clear and post_clear:
                cnt += 1
                if cnt == n:
                    return True
                # label flower so later spots can consider this
                flowerbed[i] = 1
                i += 2  # if flower, savely jump to i + 2
                continue
            i += 1  # if adjacent is flower, move to next
        return False


# %%
flowerbed = [1, 0, 0, 0, 0, 0, 1]
n = 2
Solution().canPlaceFlowers(flowerbed, n)

# %%


class Solution:
    def canPlaceFlowers(self, f, n):
        L, i, c, f = len(f) - 2, -2, 0, f + [0]
        while i < L:
            i += 2
            if f[i] == 1:
                continue
            if f[i + 1] == 0:
                c += 1
            else:
                i += 1
        return n <= c


# %%
f = [1, 0, 1, 0, 1]
Solution().canPlaceFlowers(f, 1)

# %%


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        i = 0
        n_spots = 0
        if n_spots == n:
            return True
        while i < l:
            if flowerbed[i] == 1:
                i = i + 2
                continue
            if (i == 0) and ((l == 1) or (flowerbed[i + 1] == 0)):
                n_spots += 1
                if n_spots == n:
                    return True
                flowerbed[i] = 1
                i = i + 1
            if (flowerbed[i - 1] == 0) and((i == l - 1) or (flowerbed[i + 1] == 0)):
                n_spots += 1
                if n_spots == n:
                    return True
                flowerbed[i] = 1
                i = i + 1
            i = i + 1
        return False


# %%
flowerbed = [1, 0, 1, 0, 0, 0]
n = 1
Solution().canPlaceFlowers(flowerbed, n)
