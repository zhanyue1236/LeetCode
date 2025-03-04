from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        path = []
        result = 0
        def backtracking(start_index):
            nonlocal result
            if sum(path) == target:
                result += 1
                return
            elif sum(path) > target:
                return
            for i in range(start_index, n):
                path.append(nums[i])
                backtracking(0)
                path.pop()
        backtracking(0)
        return result
S = Solution()
print(S.combinationSum4([4,2,1], 32))