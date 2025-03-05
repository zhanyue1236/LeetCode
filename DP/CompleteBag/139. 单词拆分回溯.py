from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)  # 将单词列表转换成集合，提高查找速度
        memo = {}  # 记忆化字典，记录从 start_index 开始是否能拆分
        
        def backtracking(start_index: int) -> bool:

            if start_index == n:
                return True
            
            if start_index in memo:
                return memo[start_index]
            
            for end in range(start_index + 1, n + 1):
                if s[start_index:end] in wordSet and backtracking(end):
                    memo[start_index] = True
                    return True
            
            memo[start_index] = False
            return False
        
        return backtracking(0)