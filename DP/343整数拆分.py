from typing import List
class Solution:
    #注意理解这里的dp[i]，不是指的是拆成i个数的最大乘积（这样无法进行状态转移），而是第i个数字的最大乘积！！
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        if n <= 1:
            return n
        elif n <= 3:
            return n - 1
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        print(dp)
        return dp[-1]
S = Solution()
print(S.integerBreak(10))