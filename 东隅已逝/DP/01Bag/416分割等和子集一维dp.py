from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        n = sum(nums) // 2
        dp = [0 for i in range(n + 1)]
        m = len(nums)
        for i in range(nums[0], n + 1):
            dp[i] = nums[0]
        for i in range(1, m):
            for j in range(n, -1, -1):
                if j - nums[i] >= 0:
                    #dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]) #这里会出现一个问题，就是j大的时候会用到前面已经更新过的（01背包复用），由于大不依赖小，所以可以从大到小更新
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                    if dp[j] == n:
                        #print(dp)
                        return True
            #print(dp)
        
        return False
S = Solution()
print(S.canPartition([1,5,11,5]))
