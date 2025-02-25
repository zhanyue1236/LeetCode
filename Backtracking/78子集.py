from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        n = len(nums)
        def backtracking(nums, start_index):
            result.append(path.copy())
            if start_index >= n:
                return
            for i in range(start_index, n):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()
        backtracking(nums, 0)
        return result
S = Solution()
print(S.subsets([1,2,3]))
            