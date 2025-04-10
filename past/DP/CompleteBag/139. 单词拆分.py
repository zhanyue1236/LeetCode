from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                w = s[j:i]
                if w in wordDict and dp[j] == True:
                    dp[i] = True
        
        return dp[-1]
    
S = Solution()
print(S.wordBreak("leetcode", ["leet","code"]))
        