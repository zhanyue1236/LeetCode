from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        nums = sorted(nums)
        n = len(nums)
        def backtracking(nums, start_index):
            result.append(path.copy())
            if start_index >= n:
                return
            for i in range(start_index, n):
                if i > start_index and nums[i] == nums[i - 1]: #这里的思想和40组合总数II一样，只对同层的进行修剪。
                    continue
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()
        backtracking(nums, 0)
        '''res = []
        for item in result:
            item = sorted(item)
            if item not in res:
                res.append(item)
        return res'''
        return result

S = Solution()
print(S.subsetsWithDup([1, 2, 2]))