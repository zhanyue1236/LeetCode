from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp = sum(nums)
        m = len(nums)
        if temp % 2 == 1:
            return False
        n = temp // 2
        dp = [[-1 for i in range(n + 1)] for j in range(m)]
        t = nums[0]
        for i in range(min(t,n)):
            dp[0][i] = 0
        for i in range(t, n + 1):
            dp[0][i] = t
        for i in range(m):
            dp[i][0] = 0
        for i in range(1, m):
            for j in range(1, n + 1):
                if j - nums[i] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i]) #这里出问题了，如果j - nums[i]是负数的话，他会从后往前找
                #dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i]) 这里出问题了，如果j - nums[i]是负数的话，他会从后往前找
                if n in dp[i]:
                    #print(dp)
                    return True
        #print(dp)
        if dp[-1][-1] == n:
            
            return True
        else:
            return False
        
S = Solution()
print(S.canPartition([100,4,6]))
