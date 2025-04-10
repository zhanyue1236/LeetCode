from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            #for j in range(i - 1):
                #temp = max(temp, dp[j] + nums[i])其实不用，因为dp[i - 2]的解释就是i - 2最大的价值
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

S = Solution()
print(S.rob([1,2,3,1]))