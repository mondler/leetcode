#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (54.03%)
# Likes:    4482
# Dislikes: 196
# Total Accepted:    193.9K
# Total Submissions: 359.4K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
#
#
# Example 1:
#
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
#
# Example 2:
#
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
#
# Example 3:
#
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
#
#
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def feasible(speed):
            hrs = sum([(pile - 1) // speed + 1 for pile in piles])
            return hrs <= h

        left = 1
        right = max(piles)
        while left < right:
            speed = left + (right - left) // 2
            if feasible(speed):
                right = speed
            else:
                left = speed + 1
        return left

    def bruteForce(self, piles, h):
        import math

        def hrsPerPile(pile, k):
            # if pile % k == 0:
            #     return pile // k
            # else:
            #     return pile // k + 1
            return math.ceil(pile / k)
        k = 1
        while True:
            hrs = [hrsPerPile(pile, k) for pile in piles]
            totalhrs = sum(hrs)
            if totalhrs <= h:
                return k
            else:
                k += 1
        return

# @lc code=end


piles = [3, 6, 7, 11]
h = 8

print(Solution().minEatingSpeed(piles, h))
print(Solution().bruteForce(piles, h))

piles = [30, 11, 23, 4, 20]
h = 5

print(Solution().minEatingSpeed(piles, h))
print(Solution().bruteForce(piles, h))

piles = [30, 11, 23, 4, 20]
h = 6

print(Solution().minEatingSpeed(piles, h))
print(Solution().bruteForce(piles, h))
