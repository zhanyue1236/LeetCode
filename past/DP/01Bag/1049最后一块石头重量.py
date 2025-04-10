from typing import List
class Solution:
    '''
    思路：转化，问题可以转换为将石头尽量分成两组相近的，然后进行碰撞。
    如何去做？同416分割子集，只不过没有判断，能装多少是多少（不过注意这里首先需要进行sort更正：其实也不需要） -> 01背包问题
    '''
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sorted(stones)
        m = len(stones)
        n = sum(stones) // 2
        dp = [0 for i in range(n + 1)]
        for i in range(stones[0], n + 1):
            dp[i] = stones[0]
        for i in range(1, m):
            for j in range(n, 0, -1):
                if j - stones[i] >= 0:
                    dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
            print(dp)
        return abs(sum(stones) - 2 * dp[-1])

S = Solution()
print(S.lastStoneWeightII([2,7,4,1,8,1]))
