from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = prices[0] * (-1)
        res = []
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            #dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            temp = dp[i - 1][0] + prices[i]
            if temp > dp[i - 1][1] and res:
                dp[i][1] = temp
                res.append(temp - res[-1])
            elif temp > dp[i - 1][1] and not res:
                dp[i][1] = temp
                res.append(temp)
            else:
                dp[i][1] = dp[i - 1][1]
            
        res.sort(reverse=True)
        if len(res) == 0:
            return 0
        elif len(res) == 1:
            return res[0]
        else:
            return res[0] + res[1]

S = Solution()
print(S.maxProfit([3,3,5,0,0,3,1,4]))