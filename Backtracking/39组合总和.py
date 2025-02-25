from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        def backtracking(candidates, start_index):
            if sum(path) == target:
                result.append(path.copy())
                return
            elif sum(path) > target:
                return
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                backtracking(candidates, i)
                path.pop()
        backtracking(candidates, 0)
        return result
S = Solution()
print(S.combinationSum([2,3,6,7], 7))
