from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount
        m = len(coins)
        dp = [0 for _ in range(n + 1)]
        ini = coins[0]
        for i in range(n + 1):
            if i % ini == 0:
                dp[i] = 1
        #dp[0] = 0
        for i in range(1, m):
            for j in range(n + 1):
                if j - coins[i] >= 0:
                    dp[j] += dp[j - coins[i]]

        return dp[-1]
 
S = Solution()
print(S.change(5, [1,2,5]))