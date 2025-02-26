from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        n = len(nums)
        def backtracking(nums, start_index):
            if len(path) >= 2:
                result.append(path.copy())
            if start_index >= n:
                return
            used = set()#放在这里可以进行同行之间沟通
            for i in range(start_index, n):
                if nums[i] in used:
                #if i > start_index and nums[i] == nums[i - 1]:#这里不能这么单纯的这样用，注意这个方法是基于数组已经排序完成的时候才能这样做。
                    continue
                if path and nums[i] < path[-1]:
                    continue
                else:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtracking(nums, i + 1)
                    path.pop()
        backtracking(nums, 0)
        return result
S = Solution()
print(S.findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]))