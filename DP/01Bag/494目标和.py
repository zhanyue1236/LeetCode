from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        if (S + target) < 0 or (S + target) % 2 != 0:
            return 0
        
        sumP = (S + target) // 2
        
        dp = [0] * (sumP + 1)
        dp[0] = 1   # 凑成 0 这个和，有 1 种方式：什么都不选
        
        for num in nums:
            # 这里要倒序遍历，避免重复计数
            for j in range(sumP, num - 1, -1):
                dp[j] += dp[j - num]
        
            print(dp)
        return dp[-1]
    
S = Solution()
print(S.findTargetSumWays([1,1,1,1,1], 3))