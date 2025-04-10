class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        #print(dp)
        return dp[n]


S = Solution()
print(S.fib(100))