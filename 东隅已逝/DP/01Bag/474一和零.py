from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        x = len(strs)
        # 对每个字符串统计 0 和 1 的数量
        # 这里用 [zeros, ones]
        nums = []
        for item in strs:
            zeros = item.count("0")
            ones = item.count("1")
            nums.append([zeros, ones])
        
        # dp[j][k] 表示使用若干个字符串凑出不超过 j 个 0 和 k 个 1 的最大字符串个数
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # 初始化第一项：对于第 0 个字符串
        zeros, ones = nums[0][0], nums[0][1]
        for j in range(m + 1):
            for k in range(n + 1):
                if j >= zeros and k >= ones:
                    dp[j][k] = 1
        
        # 从第 1 个字符串开始更新 dp（从后往前更新，防止重复使用同一字符串）
        for i in range(1, x):
            zeros, ones = nums[i][0], nums[i][1]
            # 注意从 m 到 0，n 到 0 都要考虑
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)
        
        # 可选：打印 dp 数组调试
        # print(dp)
        return dp[m][n]

# 测试代码
S = Solution()
print(S.findMaxForm(["10","0001","111001","1","0"], 5, 3))
