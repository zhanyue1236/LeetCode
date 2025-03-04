from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        i = 1
        while i * i <= n:
            nums.append(i * i)
            i += 1
        m = len(nums)
        dp = [99999999 for i in range(n + 1)]
        dp[0] = 1
        for i in range(m):
            for j in range(1, n + 1):
                if j - nums[i] >= 0:
                    dp[i] = min(dp[i], dp[j - nums[i]] + 1)
        return dp[-1]

