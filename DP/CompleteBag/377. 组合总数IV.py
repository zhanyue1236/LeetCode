from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m = len(nums)
        n = target
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for j in range(n + 1):
            for i in range(m):
                if j - nums[i] >= 0:#比如说2的时候，能把2挤到前面去(2,0)
                    dp[j] += dp[j - nums[i]]

        return dp[-1]
S = Solution()
print(S.combinationSum4([1,2,3],4))

#先行后列：组合数字；先列后行：排列数：对比找零钱
#从前往后完全背包；从后往前01背包
