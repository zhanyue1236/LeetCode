from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        k = int(sqrt(n)) + 1
        dp = [999999999 for i in range(k + 1)]
        for i in range(1, k + 1):
            dp[i] = i
        for i in range(k + 1):
            for j in range(k + 1):
                if j - (i ** 2) >= 0:
                    dp[j] = min(dp[j], dp[j - i ** 2] + 1)
                    
        return dp[-1]

S = Solution()
print(S.numSquares(12))