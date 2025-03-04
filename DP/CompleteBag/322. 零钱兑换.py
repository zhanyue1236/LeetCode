from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount
        dp = [99999999 for i in range(n + 1)]
        dp[0] = 0
        '''
        for i in range(n + 1):
            if i % ini == 0:
                dp[i] = i // ini
        '''
        print(dp)
        for i in range(m):
            for j in range(n + 1):
                if j - coins[i] >= 0:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
                    #print(dp)
        if dp[-1] == 99999999:
            return -1
        else:
            return dp[-1]
        
S = Solution()
print(S.coinChange([1,2,5], 11))
        