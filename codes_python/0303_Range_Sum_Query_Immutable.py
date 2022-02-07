# https://leetcode.com/problems/range-sum-query-immutable/


# %% Solution
# create a helper array to save cumulative sums

# %%

class NumArray:

    def __init__(self, nums: list[int]):
        l = len(nums)
        dp = [0] * l

        for i in range(l):
            dp[i] = dp[i - 1] + nums[i]

        self.dp = dp

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.dp[right]
        return self.dp[right] - self.dp[left - 1]

# %%

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


obj = NumArray([1, 2, 3])

print(obj.sumRange(0, 0))
print(obj.sumRange(0, 1))
print(obj.sumRange(1, 2))
print(obj.sumRange(0, 2))
