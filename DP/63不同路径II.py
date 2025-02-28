from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        elif m == 1 and n == 1:
            return 1
        elif m == 1 or n == 1:
            for item in obstacleGrid:
                if 1 in item:
                    return 0
            return 1
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break#这里是break，根本下不去
                #continue
            dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break#同理
                #continue
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]

S = Solution()
print(S.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))            
