from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # 初始化 DP 数组
        dp = [[0] * 4 for _ in range(n)]

        # 初始状态（第一天）
        dp[0][0] = -prices[0]  # 第一次买入
        dp[0][1] = 0            # 第一次卖出
        dp[0][2] = -prices[0]   # 第二次买入（可在第一次卖出后进行）
        dp[0][3] = 0            # 第二次卖出

        # 遍历每一天，更新状态
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])              # 第一次买入
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i]) # 第一次卖出
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i]) # 第二次买入
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i]) # 第二次卖出
        return dp[n - 1][3]

# 测试
S = Solution()
print(S.maxProfit([3,3,5,0,0,3,1,4]))  # 6