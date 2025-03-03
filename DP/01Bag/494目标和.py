from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sorted(nums)
        m = len(nums)
        s = sum(nums)
        if s < target:
            return 0
        #elif s == target:
            #return 1
        n = (s - target) // 2
        count = 0
        dp = [0 for i in range(n + 1)]
        for i in range(nums[0], n + 1):
            dp[i] = nums[0]
        if dp[-1] == n:
            count = 1
        for i in range(1, m):
            for j in range(n, 0, -1):
                if j == n:
                    if j - nums[i] < 0:
                        continue
                    else:
                        if dp[j] == dp[j - nums[i]] + nums[i]:
                            count += 1
                        else: 
                            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                        #if dp[j] < dp[j - nums[i]] + nums[i]:
                else:
                    if j - nums[i] < 0:
                        continue
                    else:
                        dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                        #if dp[j] < dp[j - nums[i]] + nums[i]:

        return count

S = Solution()
print(S.findTargetSumWays([1,0], 1))