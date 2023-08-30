# https://leetcode.com/problems/container-with-most-water/


# %%


class Solution:
    def maxAreaBruteForce(self, height: list[int]) -> int:
        maxWater = 0
        n = len(height)
        for i in range(n):
            for j in range(i, n):
                maxWater = max(maxWater, min(height[i], height[j]) * (j - i))
        return maxWater

    def getWater(self, l, r, height):
        return min(height[l], height[r]) * (r - l)

    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        maxWater = 0
        l = 0
        r = n - 1
        if l >= r:
            return 0
        while l < r:
            maxWater = max(maxWater, self.getWater(l, r, height))
            anchor_r = height[r]
            anchor_l = height[l]
            if height[l] <= height[r]:
                l = l + 1
                while (l < r):
                    if height[l] > anchor_l:
                        maxWater = max(maxWater, self.getWater(l, r, height))
                    if height[l] > anchor_r:
                        break
                    l = l + 1
            else:
                r = r - 1
                while (r > l):
                    if height[r] > anchor_r:
                        maxWater = max(maxWater, self.getWater(l, r, height))
                    if height[r] > anchor_l:
                        break
                    r = r - 1
        return maxWater

    def maxArea2(self, height: list[int]) -> int:
        # start from left and right, move the short height to middle
        l = 0
        r = len(height) - 1
        area = 0

        while l < r:
            area = max(area, self.getWater(l, r, height))
            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r - 1
        return area


        # %%
solution = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1, 1]
print(f'Brute Force Solution:  {solution.maxAreaBruteForce(height)}')
print(f'Best Solution 1:        {solution.maxArea(height)}')
print(f'Best Solution 2:        {solution.maxArea2(height)}')
# print(f'Min Height Index:        {solution.getMinHeightIdx(0, 8, height)}')
