from typing import List
class Solution: #组合去重问题：在单层去重，每一层需要用到一个used数组；排列问题是在一枝中去重，一个used可以重复使用，但是用完之后都要删掉。
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        n = len(nums)
        used = set()
        def backtracking(nums, start_index):
            if len(path) == n:
                result.append(path.copy())
                return
            for i in range(start_index, n):#排列问题最好把下标放进used里面，组合问题最好把数值放到used里面。
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtracking(nums, 0)
                path.pop()
                used.remove(i)
        backtracking(nums, 0)
        return result

s = Solution()
print(s.permute([1,2,3]))