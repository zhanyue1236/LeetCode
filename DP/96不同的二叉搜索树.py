'''
整体思路：查看左右子树
以3为例，如果根节点是1，那么2，3都是右子树的东西，2,3能够做成dp[2]种情况；
根节点2，左子树中有一个元素，右子树中有一个元素，能够做成dp[1] x dp[1]种情况；
根节点为3：左子树有一个元素，能够做成dp[2] x dp[0]种情况
dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[0] * dp[2]
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            temp = 0
            for j in range(i):
                temp += dp[j] * dp[i - 1 - j]
                dp[i] = temp
        #print(dp)
        return dp[-1]

S = Solution()
print(S.numTrees(3))


