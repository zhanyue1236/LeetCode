from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        temp = sum(nums)
        n = len(nums)
        if temp % 2 == 1:
            return False
        mid = temp // 2
        path = []
        flag = 0
        def backtracking(start_index):
            nonlocal flag
            if sum(path) == mid:
                flag = 1
                return True
            for i in range(start_index, n):
                path.append(nums[i])
                backtracking(i + 1)
                if flag == 1:
                    return
                path.pop()
        backtracking(0)
        return bool(flag)

S = Solution()
print(S.canPartition([1,2,5]))
