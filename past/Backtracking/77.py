from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []

        def backtracking(n, k, start_index):
            if len(path) == k:
                result.append(path.copy()) #append(path)是引用，这里需要用path.copy()
                return
            for i in range(start_index + 1, n + 1):
                path.append(i)
                backtracking(n, k, i)
                path.pop()

        backtracking(n, k, 0)
        return result

# 测试
S = Solution()
print(S.combine(4, 2))
