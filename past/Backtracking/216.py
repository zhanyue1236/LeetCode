from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        def backtracking(n, k, start_index):
            if sum(path) > n:
                return
            if len(path) == k and sum(path) == n:
                result.append(path.copy())
                return
            for i in range(start_index + 1, 10):
                path.append(i)
                backtracking(n, k, i)
                path.pop()
        backtracking(n, k, 0)
        return result