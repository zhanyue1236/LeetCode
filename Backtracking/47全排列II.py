from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        n = len(nums)
        used_coloumn = set()
        def backtracking(nums, start_index):
            if len(path) == n:
                result.append(path.copy())
                return
            used_row = set()
            for i in range(start_index, n):
                if i in used_coloumn or nums[i] in used_row:
                    continue
                used_coloumn.add(i)
                used_row.add(nums[i])
                path.append(nums[i])
                backtracking(nums, 0)
                path.pop()
                used_coloumn.remove(i)
        backtracking(nums, 0)
        return result

s = Solution()
print(s.permuteUnique([1,1,2]))

#这个题将行重复和列重复合并在了一起，因此使用两个不同的used即可。这个题也说明了前面为什么同行的方内容，同列的方下标的原因了。